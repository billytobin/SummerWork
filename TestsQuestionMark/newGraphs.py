#Billy Tobin
#Cloning, analyzing, and making x projects
#
#
import json
import matplotlib.pyplot as plt
import numpy as np
import time

from github import Github
import subprocess
import shutil
import os
from os import path
import sys

fig = plt.figure()

numOfVersions = 15
moreCount = 0
lessCount = 0
project_list = os.listdir(os.getcwd() + '\\Results\\Results5')

#print(project_list)

bigDeltaList = []
TimesOverloadedCount = []
TimesOverloadedCount1 = []
contribList = []
otherList = []


isStaticCount = [0] * numOfVersions
isnotStaticCount = [0] * numOfVersions

percentList = []
totalOverMethods = 0
totalMethods = 0
totalOverMethodsL = [0] * numOfVersions
countOfContstructs = [0] * numOfVersions
countOfNonContstructs = [0] * numOfVersions
totalList= [0]*2

#locCount = [0]*(len(project_list)-1)
locCount = [0] * numOfVersions

n = (-1)

for repo in project_list:
    #print(repo)
    

    overloadedCount = []
    x_axis = []
    y_axis = []

    if path.exists(os.getcwd() + '\\Results\\Results5\\'+repo+"\\Result0.txt"):
        n +=1
        print("hello")

    
        f = open("C:\\Users\\willi\\Summer-Work21\\Results\\Results5\\"+repo+"\\Result0.txt")
        #print(repo)
        #locCount.insert(0,0)
        

        data = json.load(f)
        

        
        for className in data:
           
            if className != "Project Wide Statistics":

                locCount[0] += (data[className]['Class Wide Statistics']["loc"])
        
                #if 'Num Of Overloaded Methods' in data[className]:
                    #totalOverMethods[0] += data[className]['Num Of Overloaded Methods']
                
                for method in data[className]:
                    if (method != 'Class Wide Statistics') and (method != 'Num Of Overloaded Methods'):
                        
                        totalOverMethodsL[0] +=data[className][method]['Times Overloaded']
                        
                        
                        #print(TimesOverloadedCount, overloadedC)
                        #TimesOverloadedCount[overloadedC] += 1
                        #TimesOverloadedCount[1] -= overloadedC
                        if data[className][method]['IsConstructor'] == True:
                            #countOfContstructs += data[className][method]['Times Overloaded']
                            countOfContstructs[0] += 1
                        else:
                            #countOfNonContstructs += data[className][method]['Times Overloaded']
                            countOfNonContstructs[0] += 1

                        if data[className][method]['isStatic'] == True:
                            #countOfContstructs += data[className][method]['Times Overloaded']
                            isStaticCount[0] += 1
                        else:
                            #countOfNonContstructs += data[className][method]['Times Overloaded']
                            isnotStaticCount[0] += 1
                #if 'Num Of Overloaded Methods' in data[className]:       
                    #TimesOverloadedCount[1] += (data[className]['Class Wide Statistics']["numberOfMethods\t"] - data[className]['Num Of Overloaded Methods'])
                #else:
                #TimesOverloadedCount[1] += data[className]['Class Wide Statistics']["numberOfMethods\t"]


    for i in range(1, numOfVersions):

    
        if path.exists("C:\\Users\\willi\\Summer-Work21\\Results\\Results5\\"+repo+"\\Result"+str(i)+".txt"):
            
            f = open("C:\\Users\\willi\\Summer-Work21\\Results\\Results5\\"+repo+"\\Result"+str(i)+".txt")
            data = json.load(f)
            #locCount.insert(0,0)
            #if type(data["Project Wide Statistics"]['Total Overloaded Methods']) == int:
                #percentList[i] += (data["Project Wide Statistics"]['Total Overloaded Methods'])
                # percentList[i] += (data["Project Wide Statistics"]['Total Overloaded Methods'] / len(project_list))
            #overloadedCount.insert(0,data["Project Wide Statistics"]["Total Overloaded Methods"])
            for className in data:
           
                if className != "Project Wide Statistics":

                    locCount[i] += (data[className]['Class Wide Statistics']["loc"])
                    
                    for method in data[className]:
                        if (method != 'Class Wide Statistics') and (method != 'Num Of Overloaded Methods'):
                        #print(method)
                            totalOverMethodsL[i] +=data[className][method]['Times Overloaded']

                            """  if (i == numOfVersions-1):
                                overloadedC = data[className][method]['Times Overloaded']
                                if len(TimesOverloadedCount1 ) < overloadedC+1:
                                    for j in range(len(TimesOverloadedCount1), overloadedC + 1):
                                        TimesOverloadedCount1.append(0)
                                #print(TimesOverloadedCount, overloadedC)
                                TimesOverloadedCount1[overloadedC] += 1
                                TimesOverloadedCount1[1] -= overloadedC """
                            if data[className][method]['IsConstructor'] == True:
                            #countOfContstructs += data[className][method]['Times Overloaded']
                                countOfContstructs[i] += 1
                            else:
                            #countOfNonContstructs += data[className][method]['Times Overloaded']
                                countOfNonContstructs[i] += 1

                            if data[className][method]['isStatic'] == True:
                            #countOfContstructs += data[className][method]['Times Overloaded']
                                isStaticCount[i] += 1
                            else:
                            #countOfNonContstructs += data[className][method]['Times Overloaded']
                                isnotStaticCount[i] += 1
                    #if (i == numOfVersions-1):
                        #if 'Num Of Overloaded Methods' in data[className]:       
                        #   TimesOverloadedCount1[1] += (data[className]['Class Wide Statistics']["numberOfMethods\t"] - data[className]['Num Of Overloaded Methods'])
                        #else:
                        #TimesOverloadedCount1[1] += data[className]['Class Wide Statistics']["numberOfMethods\t"]

   
#print(locCount)
#print(percentList)
#print(TimesOverloadedCount)
    # if y_axis[numOfVersions-1]-y_axis[0] >= 0:
    #     moreCount+= 1
    # else:
    #     lessCount +=1

    #if repo != "CircleImageView":
     #   percentList[0] -= y_axis[7]   

    # for j in range(0, len(overloadedCount)):
    #     if overloadedCount[j] == None:
    #         overloadedCount[j] = 0.0
    # deltaList = []
    # for j in range(0, len(overloadedCount)-1):
    #     deltaList.append(overloadedCount[j+1] - overloadedCount[j])
    # #print(repo + str(deltaList))
    # if bigDeltaList == []:
    #     for i in deltaList:
    #         bigDeltaList.append(i/ len(project_list))
    # else:
    #     for i in range(0, len(deltaList)):
    #         bigDeltaList[i] += (abs(deltaList[i])/ len(project_list))
       
    
            
        # xaxis = x_axis[1:]
        # newX = []
        # for i in xaxis:
        #     newX.append(str(i))
        # plt.bar(newX, deltaList)
        # plt.xlabel('Commits Ago (oldest to newest)')
        # plt.ylabel('Num of Overloaded Methods Added')
        # plt.title('Delta Graph for Different Versions of '+ repo)
        # dir = "C:\\Users\\willi\\Summer-Work21\\Results\\Graphs4\\" +repo
        # #if not os.path.exists(dir):
        #     os.mkdir(dir)
        # plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs4\\'+repo+'\\Delta.png')
        # plt.clf()
    #plt.plot(['Start','End'], [y_axis[0],y_axis[14]])
        # plt.xlim(max(x_axis),min(x_axis))

        # plt.xlabel('Commits ago -- (Older to Newer)')  # Add an x-label to the axes.
        # plt.ylabel('Percentage of Overloaded Methods')
        # plt.title(repo)  # Add a title to the axes.
        # #plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Results1.2\\RxJava\\graph.png')
        
        # plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs4\\'+repo+'\\Percent.png')

        # plt.clf()
        # plt.plot(x_axis, overloadedCount)
        # plt.xlim(max(x_axis),min(x_axis))

        # plt.xlabel('Commits ago -- (Older to Newer)')  # Add an x-label to the axes.
        # plt.ylabel('Number of Overloaded Methods')
        # plt.title(repo)  # Add a title to the axes.
    #plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs4\\allRepos1.png')
        # plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs4\\'+repo+'\\Total.png')


fig = plt.figure() 
#print(countOfContstructs, countOfNonContstructs)
#print(totalOverMethods)
'''
plt.pie([countOfContstructs[0]/len(project_list), countOfNonContstructs[0]/len(project_list)], labels=['Constructors', 'Non-Constructors'], colors=['lightcoral', 'lightskyblue'], autopct='%1.1f%%' )
plt.title('Avg. Num of Overloaded methods that are Constructors vs NonCostructors at current stage')
plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs4\\ConstructorsVSNonConstrucors_allCalls_Current.png')
plt.clf()

plt.pie([countOfContstructs[numOfVersions-1]/len(project_list), countOfNonContstructs[numOfVersions-1]/len(project_list)], labels=['Constructors', 'Non-Constructors'], colors=['lightcoral', 'lightskyblue'], autopct='%1.1f%%' )
plt.title('Avg. Num of Overloaded methods that are Constructors vs NonCostructors at beginning')
plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs4\\ConstructorsVSNonConstrucors_allCalls_beg.png')
plt.clf()
#print((contribList), (percentList))
#xs, ys = zip(*sorted(zip(contribList, percentList)))

'''

for i in range(numOfVersions):
    locCount[i]/=len(project_list)
    totalOverMethodsL[i]/=len(project_list)

plt.plot(locCount, totalOverMethodsL)
#plt.plot(contribList, percentList)
plt.title('Average lines of code vs Average Number of Overloaded methods')
plt.xlabel('Average LOC at Different Points in LifeSpan')
plt.ylabel('Average Number of Overloaded Methods')
plt.show()

'''

plt.clf()
print((otherList), (locCount))
#xs, ys = zip(*sorted(zip(contribList, percentList)))

#for i in range(len(otherList)):
#    otherList[i] = otherList[i] / locCount[i]
plt.title("Contributors vs num of overloaded methods")
plt.xlabel('Num of Contributors')
plt.ylabel('Number of Overloaded Methods/LOC')
plt.scatter(contribList, otherList)
plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs4\\ContribsTotal.png')

plt.close(fig)


numberedList = []
for i in range(len(isStaticCount)):
    numberedList.append(i)

plt.plot(numberedList, isStaticCount, label="Static Methods")
plt.plot(numberedList, isnotStaticCount, label="Non-Static Methods")
plt.xlim(max(numberedList),min(numberedList))
plt.legend()
#plt.plot(contribList, percentList)
plt.title('The change of static and non static overloaded methods over time.')
plt.xlabel('Stage of Project Life')
plt.ylabel('Number of Static and nonSttticOverloaded Methods')
plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs4\\staticVSnonStatic.png')
'''
'''
labelList = []
for i in range(len(TimesOverloadedCount)):
    labelList.append(i)

labelList1 = []
for i in range(len(TimesOverloadedCount1)):
    labelList1.append(i)

#print(len(TimesOverloadedCount), len(labelList))

plt.clf()
plt.pie(TimesOverloadedCount, labels = labelList )
plt.title('Number of Times a Method is Overloaded in Current Times')
plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs4\\TimesOverloadedFrequencyCurrent.png')
plt.clf()
plt.pie(TimesOverloadedCount1, labels = labelList1 )
plt.title('Number of Times a Method is Overloaded At beginning of Projects')
plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs4\\TimesOverloadedFrequencyBeginning.png')
plt.clf()
# plt.clf()
 
 #plt.bar([1,2,3,4,5,6,7,8,9,10,11,12,13,14], bigDeltaList)
# #plt.title('Change in Overloaded Methods Across Many Projects')
# #plt.xlabel('Stage in Lifespan (Older to Newer)')
# #plt.ylabel('Num of Overloaded Methods Taken/Added')
# #plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs4\\genTest.png')

'''
# plt.close(fig)
#print(totalOverMethods / totalMethods, totalOverMethods)
#print(locCount)
#print(totalOverMethodsL)