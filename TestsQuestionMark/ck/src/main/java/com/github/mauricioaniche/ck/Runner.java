package com.github.mauricioaniche.ck;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.eclipse.jdt.core.dom.Modifier;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;
import java.util.ArrayList;
import java.util.List;

public class Runner {

	public static void main(String[] args) throws IOException {

		if (args == null || args.length < 1) {
			System.out.println("Usage java -jar ck.jar <path to project> <use Jars=true|false> <max files per partition, 0=automatic selection> <print variables and fields metrics? True|False> <commit Number>");
			System.exit(1);
		}

		String path = args[0];

		// use jars?
		boolean useJars = false;
		if(args.length >= 2)
			useJars = Boolean.parseBoolean(args[1]);

		// number of files per partition?
		int maxAtOnce = 0;
		if(args.length >= 3)
			maxAtOnce = Integer.parseInt(args[2]);

		// variables and field results?
		boolean variablesAndFields = true;
		if(args.length >= 4)
			variablesAndFields = Boolean.parseBoolean(args[3]);
		
		int commitNum = 0;
		if(args.length >= 5)
			commitNum = Integer.parseInt(args[4]);
		
		
		String ProjUrl = args[5];
		String commitHash = args[6];
		int numContribs = 0;
		if(args.length >= 5)
			numContribs = Integer.parseInt(args[7]);



		//ResultWriter writer = new ResultWriter("class.csv", "method.csv", "variable.csv", "field.csv", variablesAndFields);
		JSONObject array = new JSONObject();
		File outputFile = new File("output.txt");
		FileWriter outputFileWriter = new FileWriter("output.txt", true);
		outputFile.createNewFile();
		JSONObject obj = new JSONObject();
		//obj.put("Total Number of Methods:", new Integer(0));
		List<Integer> totalCount = new ArrayList<>();
		List<Integer> overLoadedCount = new ArrayList<>();


		new CK(useJars, maxAtOnce, variablesAndFields).calculate(path, new CKNotifier() {
			@Override
			public void notify(CKClassResult result) {

				
				totalCount.add(result.getNumberOfMethods());

				HashMap<String[], Object[]> map = new HashMap<>();
				
				for (CKMethodResult method : result.getMethods()) {
					//System.out.println(method.toString());
					Object[] arr = new Object[36]; // 0 = count, 1 = parameters, 2 = Visibility, 3 = isFinal, 4=isProtected, 5=isStatic
					String name="";
					String parameters="";
					for (int i = 0; i < method.getMethodName().length(); i++) {
						if (method.getMethodName().charAt(i) == '/'){
							for (int j = i+1; j < method.getMethodName().length(); j++ ){
								parameters = parameters + (method.getMethodName().charAt(j));
							}
							break;
						} else {
							name = name + (method.getMethodName().charAt(i));
						}
					}


					arr[2] = Modifier.isPrivate(method.getModifiers());
					arr[3] = Modifier.isFinal(method.getModifiers());
					arr[4] = Modifier.isProtected(method.getModifiers());
					arr[5] = Modifier.isStatic(method.getModifiers());
					arr[6] = method.getCbo();
					arr[7] = method.getRfc();
					arr[8] = method.getWmc();
					arr[9] = method.getMethodName();
					arr[10] = method.getQualifiedMethodName();
					arr[11] = method.getIsVisible();
					arr[12] = method.getParametersQty();
					arr[13] = method.getReturnQty();
					arr[14] = method.getLoc();
					arr[15] = method.getVariablesQty();
					arr[16] = method.getVariablesUsage();
					arr[17] = method.getStartLine();
					arr[18] = method.getLoopQty();
					arr[19] = method.getComparisonsQty();
					arr[20] = method.getTryCatchQty();
					arr[21] = method.getParenthesizedExpsQty();
					arr[22] = method.getStringLiteralsQty();
					arr[23] = method.getNumbersQty();
					arr[24] = method.getAssignmentsQty();
					arr[25] = method.getMathOperationsQty();
					arr[26] = method.getMaxNestedBlocks();
					arr[27] = method.getAnonymousClassesQty();
					arr[28] = method.getInnerClassesQty();
					arr[29] = method.getLambdasQty();
					arr[30] = method.getUniqueWordsQty();
					arr[31] = method.getFieldUsage();
					arr[32] = method.isConstructor();
					arr[33] = method.getModifiers();
					arr[34] = method.getLogStatementsQty();
					arr[35] = method.getHasJavadoc();

					String[] temp = {result.getClassName(), name};
					boolean found = false;
					for (String[] i : map.keySet()) {
						if (Arrays.equals(i, temp)) {
							Object[] oldArr = map.get(i);
							int num = (Integer)oldArr[0];
							num += 1;
							oldArr[0] = num;
							String[] arrOfPara = (String[])oldArr[1];
							String[] newArrOfPara = Arrays.copyOf(arrOfPara, arrOfPara.length + 1);
							newArrOfPara[newArrOfPara.length - 1] = parameters;
							oldArr[1] = newArrOfPara;
							map.replace(i, oldArr);							
							found = true;
							oldArr = null;

						}

					} 
					if (found==false){
						arr[0] = new Integer(1);
						arr[1] = new String[]{parameters};
						map.put(temp, arr);
						
					}
					parameters = "";
				}
				
				int count = 0;
				JSONObject classes = new JSONObject();
				//System.out.println(map);
				for (String[] i : map.keySet()) {
					JSONObject methods = new JSONObject();
					int num = (Integer)map.get(i)[0];
					//int num = 2;
					if (num>0){ //should be more than 0 (this represents how many times method was overlaoded)
						//System.out.println(map);
						count+=1;
						
						methods.put("Times Overloaded", map.get(i)[0]);
						methods.put("isPrivate", map.get(i)[2]);
						methods.put("isFinal", map.get(i)[3]);
						methods.put("isProtected", map.get(i)[4]);
						methods.put("isStatic", map.get(i)[5]);
						methods.put("Cbo", map.get(i)[6]);
						methods.put("Rfc", map.get(i)[7]);
						methods.put("Wmc", map.get(i)[8]);
						methods.put("MethodName", map.get(i)[9]);
						methods.put("QualifiedMethodName", map.get(i)[10]);
						methods.put("IsVisible", map.get(i)[11]);
						methods.put("ParametersQty", map.get(i)[12]);
						methods.put("ReturnQty", map.get(i)[13]);
						methods.put("Loc", map.get(i)[14]);
						methods.put("VariablesQty", map.get(i)[15]);
						//methods.put("VariablesUsage", map.get(i)[16]);
						methods.put("StartLine", map.get(i)[17]);
						methods.put("LoopQty", map.get(i)[18]);
						methods.put("ComparisonsQty", map.get(i)[19]);
						methods.put("TryCatchQty", map.get(i)[20]);
						methods.put("ParenthesizedExpsQty", map.get(i)[21]);
						methods.put("LiteralsQty", map.get(i)[22]);
						methods.put("NumbersQty", map.get(i)[23]);
						methods.put("AssignmentsQty", map.get(i)[24]);
						methods.put("MathOperationsQty", map.get(i)[25]);
						methods.put("MaxNestedBlocks", map.get(i)[26]);
						methods.put("AnonymousClassesQty", map.get(i)[27]);
						methods.put("InnerClassesQty", map.get(i)[28]);
						methods.put("LambdasQty", map.get(i)[29]);
						methods.put("UniqueWordsQty", map.get(i)[30]);
						//methods.put("FieldUsage", map.get(i)[31]);
						methods.put("IsConstructor", map.get(i)[32]);
						methods.put("Modifiers", map.get(i)[33]);
						methods.put("LogStatementsQty", map.get(i)[34]);
						methods.put("HasJavadoc", map.get(i)[35]);

						JSONArray sigArray = new JSONArray();
						
						for (int j = 0; j < (Integer)map.get(i)[0]; j++){
							String[] array = (String[])map.get(i)[1];
							sigArray.add(array[j]);
						}
						methods.put("Different input Parameters",sigArray);
						classes.put(i[1], methods);
							}					
					}

					
					if (classes.isEmpty() == false){
						overLoadedCount.add(count);
						classes.put("Num Of Overloaded Methods", count);
						
					
					}	
					JSONObject classStats = new JSONObject();						
					classStats.put("file", result.getFile());	
					classStats.put("className",result.getClassName());	
					classStats.put("type",result.getType());	
					classStats.put("dit", result.getDit());	
					classStats.put("wmc", result.getWmc());	
					classStats.put("cbo",result.getCbo());	
					classStats.put("lcom", result.getLcom());	
					classStats.put("rfc",result.getRfc());	
					classStats.put("nosi",result.getNosi());	
					classStats.put("loc", result.getLoc());		
						
					classStats.put("returnQty", result.getReturnQty());	
					classStats.put("loopQty", result.getLoopQty());	
					classStats.put("comparisonsQty", result.getComparisonsQty());	
					classStats.put("tryCatchQty", result.getTryCatchQty());	
					classStats.put("parenthesizedExpsQty", result.getParenthesizedExpsQty());	
					classStats.put("StringLiteralsQty", result.getStringLiteralsQty());	
					classStats.put("numbersQty", result.getNumbersQty());	
					classStats.put("assignmentsQty", result.getAssignmentsQty());	
					classStats.put("mathOperationsQty", result.getMathOperationsQty());	
					classStats.put("variablesQty", result.getVariablesQty());	
					classStats.put("maxNestedBlocks", result.getMaxNestedBlocks());	
					classStats.put("anonymousClassesQty", result.getAnonymousClassesQty());	
					classStats.put("innerClassesQty", result.getInnerClassesQty());	
					classStats.put("lambdasQty", result.getLambdasQty());	
					classStats.put("uniqueWordsQty", result.getUniqueWordsQty());	
					classStats.put("numberOfMethods	", result.getNumberOfMethods());
					classStats.put("numberOfStaticMethods", result.getNumberOfStaticMethods());	
					classStats.put("numberOfPublicMethods", result.getNumberOfPublicMethods());	
					classStats.put("numberOfMethods", result.getNumberOfMethods());	
					classStats.put("numberOfProtectedMethods",result.getNumberOfProtectedMethods());	
					classStats.put("numberOfDefaultMethods", result.getNumberOfDefaultMethods());	
					classStats.put("numberOfAbstractMethods", result.getNumberOfAbstractMethods());	
					classStats.put("numberOfFinalMethods", result.getNumberOfFinalMethods());	
					classStats.put("numberOfSynchronizedMethods", result.getNumberOfSynchronizedMethods());	
					classStats.put("numberOfFields", result.getNumberOfFields());	
					classStats.put("numberOfStaticFields", result.getNumberOfStaticFields());	
					classStats.put("numberOfPublicFields", result.getNumberOfPublicFields());	
					classStats.put("numberOfFields",result.getNumberOfFields());	
					classStats.put("numberOfFields", result.getNumberOfFields());	
					classStats.put("numberOfProtectedFields", result.getNumberOfProtectedFields());	
					classStats.put("numberOfDefaultFields", result.getNumberOfDefaultFields());	
					classStats.put("numberOfFinalFields", result.getNumberOfFinalFields());	
					classStats.put("numberOfSynchronizedFields", result.getNumberOfSynchronizedFields());	
					classStats.put("modifiers",	result.getModifiers());
					classStats.put("numberOfLogStatements", result.getNumberOfLogStatements());	
					classStats.put("tightClassCohesion", result.getTightClassCohesion());	
					classStats.put("looseClassCohesion", result.getLooseClassCohesion());	

					classes.put("Class Wide Statistics", classStats);
					obj.put(result.getClassName(), classes);
					//int tempNum = obj.getInt("Total Number of Methods:");
					//obj.put("Total Number of Methods:", obj.get("Total Number of Methods:") + count);		  
			}
			
			

			@Override
			public void notifyError(String sourceFilePath, Exception e) {
				System.err.println("Error in " + sourceFilePath);
				e.printStackTrace(System.err);
			}
		});
		double sum = 0;
			for (int i = 0; i < totalCount.size() ; i++) {
				sum += totalCount.get(i);
			}
			int sum1 = 0;
			for (int k = 0; k < overLoadedCount.size() ; k++) {
				sum1 += totalCount.get(k);
			}


			JSONObject stats = new JSONObject();
			stats.put("Total Methods", sum);
			stats.put("Total Overloaded Methods", sum1);
			double percentage = (sum1 / sum);
			stats.put("percentage of overloaded", percentage);
			stats.put("Commit Number", commitNum);
			stats.put("Project URL", ProjUrl);
			stats.put("Commit Hash", commitHash);
			if (numContribs != 0)
				stats.put("Number of Contributors", numContribs);
			obj.put("Project Wide Statistics", stats);

		outputFileWriter.write(obj.toJSONString());
		outputFileWriter.close();
		//writer.flushAndClose();
	}
}
