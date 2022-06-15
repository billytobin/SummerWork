
import json
from msilib.schema import Error

import re
import matplotlib.pyplot as plt
import numpy as np
import time
from statistics import mean, median
import Levenshtein
import random

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
project_list = os.listdir(os.getcwd() + '\\TestsQuestionMark\\CurrentResults\\results')
otherplist = os.listdir(os.getcwd() + '\\Results\\CurrentAnalysis')

project_list+= otherplist
#C:\Users\willi\Summer-Work21\TestsQuestionMark\CurrentResults\results\btrace-master
print(len(project_list))
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

n = (0)
totDists =[]
array = []
dists = []
#rint(Levenshtein.distance("hello", "hell"))
dict = {}

for repo in project_list:
    #
    # print(repo)
    

    overloadedCount = 0
    totalCount =0
    x_axis = []
    y_axis = []

    

    if True:
        n +=1
        
        try:
            f = open(os.getcwd() + '\\TestsQuestionMark\\CurrentResults\\results\\'+repo+"\\analysis.json")
        except FileNotFoundError:
            f = open(os.getcwd() + '\\Results\\CurrentAnalysis\\' + repo+'\\Result0.txt')
        #print(repo)
        #locCount.insert(0,0)        
        try:
            data = json.load(f)
        
            for className in data:
                dict = {}
                array=[]
            #We are now in a class
                if className != "Project Wide Statistics":

                    
                    for method in data[className]:
                        
                        #We are now in each method
                        if (method != 'Class Wide Statistics') and (method != 'Num Of Overloaded Methods'):
                            #do stuff
                            if data[className][method]['Times Overloaded'] != 1:
                                totalOverMethods +=data[className][method]['Times Overloaded']
                                #dict.append(data[className][method]['Different input Parameters'], [method])

                            if data[className][method]['Times Overloaded'] == 1:
                                inputparams = str (data[className][method]['Different input Parameters'])
                                #print(inputparams)
                                if inputparams in dict:
                                    dict[inputparams].append(method)
                                    #print(dict,"\n\n\n")
                                else:
                                    dict[inputparams] = [method]
                                    #print(dict)

                            array.append(method)
                
                            totalMethods += data[className][method]['Times Overloaded']
                            #print(dict[inputparams])
                    #now we run the distance analysis as array is all of the methods in a certain class
                    for i in dict:
                        if len(dict[i]) != 1:
                            for j in range(len(dict[i])):
                                for k in range(j+1, len(dict[i])):
                                    #print(j,k)
                                    #if Levenshtein.distance(dict[i][j],dict[i][k]) > 30:
                                    # print(dict[i][j],dict[i][k])
                                     #   pass
                                    dists.append(Levenshtein.distance(dict[i][j],dict[i][k]))
                    #  for j in range(i, len(array)):
                    #      if i !=j:
                    for i in range(len(array)):
                        for j in range(i+1, len(array)):
                            totDists.append(Levenshtein.distance(array[i],array[j]))
                            
                    '''
                    repeat =[]
                    for i in dict:
                        repeat.append(i)
                        for k in dict[i]:
                            for j in dict:
                                if j not in repeat:
                                    for l in dict[j]:
                                        totDists.append(Levenshtein.distance(k,l))
                    '''#          pass
        except UnicodeDecodeError:
            pass
            #print(dict)
print(mean(dists))
print(median(dists)) 



'''
count = 0
for i in range(0,len(array),5):
    for j in range(i+1, len(array)):
        count +=1
        totDists.append(Levenshtein.distance(array[i], array[j]))
''''''
randomlist = []
for i in range(0,5000):
    n = random.randint(0,len(array)-1)
    randomlist.append(array[n])

for i in range(len(randomlist)):
    for j in range(i+1, len(randomlist)):
        totDists.append(Levenshtein.distance(array[i], array[j]))'''

print(mean(totDists))
print(median(totDists)) 

                #save the results
                #then we reset array

#print(countOfContstructs, countOfNonContstructs)
#print(totalOverMethods)
#fig = plt.figure(figsize =(10, 7))
# f = open("demofile2.txt", "w")
# for i in totDists:

#    f.write(str(i)+',')
# f.close()

# Creating plot

#fig, axs = plt.subplots(1, 2)
fig = plt.figure(figsize =(10, 7))
 
# Creating plot
plt.boxplot(dists)
plt.title('Edit Distance between method with similar signatures')
#plt.xlabel('Average LOC at Different Points in LifeSpan')
plt.ylabel('Edit distance between methods')
plt.ylim([0,70]) 
 
# show plot
#plt.show()

plt.savefig('C:\\Users\\willi\\Summer-Work21\\dists')


fig = plt.figure(figsize =(10, 7))
 
# Creating plot
plt.boxplot(totDists)
plt.title('Edit Distance between method with non-similar signatures')
#plt.xlabel('Average LOC at Different Points in LifeSpan')
plt.ylabel('Edit distance between methods')
plt.ylim([0,70])

plt.savefig('C:\\Users\\willi\\Summer-Work21\\todDists')
 

# We can set the number of bins with the *bins* keyword argument.
'''
plt.hist(dists, density=True, bins=20)  # density=False would make counts
axs[0].hist(dists, bins=20)
axs[1].hist(totDists, bins=20)
#plt.ylabel('Probability')
#plt.xlabel('Data')
 '''
# show plot
#plt.show()
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


fig = plt.figure() 

#plt.plot(contribList, percentList)
plt.title('Average lines of code vs Number of Overloaded methods')
plt.xlabel('Average LOC at Different Points in LifeSpan')
plt.ylabel('Number of Overloaded Methods')
plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs3\\TrueLOCvsOverL.png')


plt.plot(locCount, totalOverMethodsL)
#plt.plot(contribList, percentList)
plt.title('Average lines of code vs Number of Overloaded methods')
plt.xlabel('Average LOC at Different Points in LifeSpan')
plt.ylabel('Number of Overloaded Methods')
plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs3\\TrueLOCvsOverL.png')'''