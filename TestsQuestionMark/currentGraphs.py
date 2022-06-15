#  #Billy Tobin

# #Current graphs
# #
# #

# import json

# import matplotlib.pyplot as plt
# import numpy as np
# import time
# from statistics import mean, median
# import Levenshtein
# import random

# from github import Github
# import subprocess
# import shutil
# import os
# from os import path
# import sys


# fig = plt.figure()

# numOfVersions = 15
# moreCount = 0
# lessCount = 0
# project_list = os.listdir(os.getcwd() + '\\TestsQuestionMark\\CurrentResults\\results')
# #C:\Users\willi\Summer-Work21\TestsQuestionMark\CurrentResults\results\btrace-master

# #print(project_list)

# bigDeltaList = []
# TimesOverloadedCount = []
# TimesOverloadedCount1 = []
# contribList = []
# otherList = []


# isStaticCount = [0] * numOfVersions
# isnotStaticCount = [0] * numOfVersions

# percentList = []
# totalOverMethods = 0
# totalMethods = 0
# totalOverMethodsL = [0] * numOfVersions
# countOfContstructs = [0] * numOfVersions
# countOfNonContstructs = [0] * numOfVersions
# totalList= [0]*2

# #locCount = [0]*(len(project_list)-1)
# locCount = [0] * numOfVersions

# n = (-1)
# totDists =[]
# array = []
# dists = []
# #rint(Levenshtein.distance("hello", "hell"))

# for repo in project_list:
#     #
#     # print(repo)
    

#     overloadedCount = 0
#     totalCount =0
#     x_axis = []
#     y_axis = []

#     if path.exists(os.getcwd() + '\\TestsQuestionMark\\CurrentResults\\results\\'+repo+"\\analysis.json"):
#         n +=1
        
    
#         f = open(os.getcwd() + '\\TestsQuestionMark\\CurrentResults\\results\\'+repo+"\\analysis.json")
#         #print(repo)
#         #locCount.insert(0,0)
        
#         try:
#             data = json.load(f)
        
#             for className in data:
#                 dict = {}
#                 array=[]
#             #We are now in a class
#                 if className != "Project Wide Statistics":

                    
#                     for method in data[className]:
                        
#                         #We are now in each method
#                         if (method != 'Class Wide Statistics') and (method != 'Num Of Overloaded Methods'):
#                             #do stuff
#                             if data[className][method]['Times Overloaded'] != 1:
#                                 totalOverMethods +=data[className][method]['Times Overloaded']
#                                 overloadedCount +=data[className][method]['Times Overloaded']
#                                 #dict.append(data[className][method]['Different input Parameters'], [method])

                            
#                             totalCount +=data[className][method]['Times Overloaded']
#                             totalMethods += data[className][method]['Times Overloaded']
#                             #print(dict[inputparams])
#                     #now we run the distance analysis as array is all of the methods in a certain class
                   
                            
                    
#                     repeat =[]
#                     for i in dict:
#                         repeat.append(i)
#                         for k in dict[i]:
#                             for j in dict:
#                                 if j not in repeat:
#                                     for l in dict[j]:
#                                         totDists.append(Levenshtein.distance(k,l))
#                     #          pass
#             if totalCount != 0:
            
#                 otherList.append(overloadedCount/totalCount)
#         except UnicodeDecodeError:
#             pass
#             #print(dict)


#                 #save the results
#                 #then we reset array

# #print(countOfContstructs, countOfNonContstructs)
# #print(totalOverMethods)
# #fig = plt.figure(figsize =(10, 7)
# # Creating plot

# #fig, axs = plt.subplots(1, 2)
# fig = plt.figure(figsize =(10, 7))
# print(mean(otherList))
# print(totalOverMethods/totalMethods)
# # Creating plot
# plt.boxplot(otherList)
# plt.title('Percentage of Methods that are Currently Overloaded in Top Repositories')
# #plt.xlabel('Average LOC at Different Points in LifeSpan')
# plt.ylabel('Percentage of overloaded methods')

 
# # show plot
# plt.show()

# #plt.savefig('C:\\Users\\willi\\Summer-Work21\\dists')

 

# # We can set the number of bins with the *bins* keyword argument.

# plt.hist(dists, density=True, bins=20)  # density=False would make counts
# axs[0].hist(dists, bins=20)
# axs[1].hist(totDists, bins=20)
# #plt.ylabel('Probability')
# #plt.xlabel('Data')
#  '''
# # show plot
# #plt.show()
# '''
# plt.pie([countOfContstructs[0]/len(project_list), countOfNonContstructs[0]/len(project_list)], labels=['Constructors', 'Non-Constructors'], colors=['lightcoral', 'lightskyblue'], autopct='%1.1f%%' )
# plt.title('Avg. Num of Overloaded methods that are Constructors vs NonCostructors at current stage')
# plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs4\\ConstructorsVSNonConstrucors_allCalls_Current.png')
# plt.clf()

# plt.pie([countOfContstructs[numOfVersions-1]/len(project_list), countOfNonContstructs[numOfVersions-1]/len(project_list)], labels=['Constructors', 'Non-Constructors'], colors=['lightcoral', 'lightskyblue'], autopct='%1.1f%%' )
# plt.title('Avg. Num of Overloaded methods that are Constructors vs NonCostructors at beginning')
# plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs4\\ConstructorsVSNonConstrucors_allCalls_beg.png')
# plt.clf()
# #print((contribList), (percentList))
# #xs, ys = zip(*sorted(zip(contribList, percentList)))


# fig = plt.figure() 

# #plt.plot(contribList, percentList)
# plt.title('Average lines of code vs Number of Overloaded methods')
# plt.xlabel('Average LOC at Different Points in LifeSpan')
# plt.ylabel('Number of Overloaded Methods')
# plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs3\\TrueLOCvsOverL.png')


# plt.plot(locCount, totalOverMethodsL)
# #plt.plot(contribList, percentList)
# plt.title('Average lines of code vs Number of Overloaded methods')
# plt.xlabel('Average LOC at Different Points in LifeSpan')
# plt.ylabel('Number of Overloaded Methods')
# plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs3\\TrueLOCvsOverL.png')


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

                array=[]
            #We are now in a class
                if className != "Project Wide Statistics":

                    
                    for method in data[className]:
                        
                        #We are now in each method
                        if (method != 'Class Wide Statistics') and (method != 'Num Of Overloaded Methods'):
                            #do stuff
                            if data[className][method]['Times Overloaded'] != 1:
                                if data[className][method]['Times Overloaded'] in dict:
                                    dict[data[className][method]['Times Overloaded']] +=1
                                elif data[className][method]['Times Overloaded'] >= 7:
                                    if "More than 7" in dict:
                                        dict["More than 7"] += 1
                                    else:
                                        dict["More than 7"] = 1
                                else:        
                                    dict[data[className][method]['Times Overloaded']] = 1
                                #dict.append(data[className][method]['Different input Parameters'], [method])

                            
                            totalCount +=data[className][method]['Times Overloaded']
                            totalMethods += data[className][method]['Times Overloaded']
                            #print(dict[inputparams])
                    #now we run the distance analysis as array is all of the methods in a certain class
                   
                            
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
            if totalCount != 0:
            
                otherList.append(overloadedCount/totalCount)
        except UnicodeDecodeError:
            pass
            #print(dict)


                #save the results
                #then we reset array

#print(countOfContstructs, countOfNonContstructs)
#print(totalOverMethods)
#fig = plt.figure(figsize =(10, 7)
# Creating plot

#fig, axs = plt.subplots(1, 2)
#fig = plt.figure(figsize =(10, 7))
#print(mean(otherList))
#print(totalOverMethods/totalMethods)
# Creating plot
l1=[]
l2=[]
print(dict)
for i in dict:
    
    l1.append(i)
    l2.append(dict[i])

#l1.sort()
#l2.sort()

plt.pie(x=l2, labels=l1, autopct='%1.1f%%')
plt.title('Distribution of How Many Times a Method is Overloaded')
#plt.xlabel('Average LOC at Different Points in LifeSpan')


 
# show plot
plt.show()

#plt.savefig('C:\\Users\\willi\\Summer-Work21\\dists')

 

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

 #Billy Tobin

#Current graphs
#
#

# import json
# from msilib.schema import Error

# import re
# import matplotlib.pyplot as plt
# import numpy as np
# import time
# from statistics import mean, median
# import Levenshtein
# import random

# from github import Github
# import subprocess
# import shutil
# import os
# from os import path
# import sys


# fig = plt.figure()

# numOfVersions = 15
# moreCount = 0
# lessCount = 0
# project_list = os.listdir(os.getcwd() + '\\TestsQuestionMark\\CurrentResults\\results')
# otherplist = os.listdir(os.getcwd() + '\\Results\\CurrentAnalysis')

# project_list+= otherplist
# #C:\Users\willi\Summer-Work21\TestsQuestionMark\CurrentResults\results\btrace-master
# print(len(project_list))
# #print(project_list)

# bigDeltaList = []
# TimesOverloadedCount = []
# TimesOverloadedCount1 = []
# contribList = []
# otherList = []


# isStaticCount = [0] * numOfVersions
# isnotStaticCount = [0] * numOfVersions

# percentList = []
# totalOverMethods = 0
# totalMethods = 0
# totalOverMethodsL = [0] * numOfVersions
# countOfContstructs = [0] * numOfVersions
# countOfNonContstructs = [0] * numOfVersions
# totalList= [0]*2

# #locCount = [0]*(len(project_list)-1)
# locCount = [0] * numOfVersions

# n = (0)
# totDists =[]
# array = []
# dists = []
# #rint(Levenshtein.distance("hello", "hell"))
# dict = {}

# for repo in project_list:
#     #
#     # print(repo)
    

#     overloadedCount = 0
#     totalCount =0
#     x_axis = []
#     y_axis = []

    

#     if True:
#         n +=1
        
#         try:
#             f = open(os.getcwd() + '\\TestsQuestionMark\\CurrentResults\\results\\'+repo+"\\analysis.json")
#         except FileNotFoundError:
#             f = open(os.getcwd() + '\\Results\\CurrentAnalysis\\' + repo+'\\Result0.txt')
#         #print(repo)
#         #locCount.insert(0,0)
        
#         try:
#             data = json.load(f)
        
#             for className in data:
                
#                 array=[]
#             #We are now in a class
#                 if className != "Project Wide Statistics":

#                     temptict = {}


#                     for method in data[className]:
                        
#                         #We are now in each method
#                         if (method != 'Class Wide Statistics') and (method != 'Num Of Overloaded Methods'):
#                             #do stuff
#                             if data[className][method]['Times Overloaded'] != 1:
#                                 #totalOverMethods +=data[className][method]['Times Overloaded']
#                                 #overloadedCount +=data[className][method]['Times Overloaded']
#                                 #dict.append(data[className][method]['Different input Parameters'], [method])
#                                 num = str(data[className][method]['Different input Parameters'])
#                                 #print(num)

#                                 pattern="'\d+"
#                                 nums1=str(re.findall(pattern,num))
#                                 #print(nums1)
#                                 pattern="\d+"
#                                 nums=re.findall(pattern,nums1)

#                                 numList=[int(i) for i in nums]
#                                 numList.sort()
#                                # print(numList)
                               
#                                 for i in range(1, len(numList)):
#                                     newNum = int(numList[i]) - int(numList[0])
                                    

#                                     if newNum in dict:
#                                         dict[newNum] +=1
#                                     else:
#                                         dict[newNum] = 1



                            
#                             #totalCount +=data[className][method]['Times Overloaded']
#                             #totalMethods += data[className][method]['Times Overloaded']
#                             #print(dict[inputparams])
#                     #now we run the distance analysis as array is all of the methods in a certain class
                   
                            
#                     '''
#                     repeat =[]
#                     for i in dict:
#                         repeat.append(i)
#                         for k in dict[i]:
#                             for j in dict:
#                                 if j not in repeat:
#                                     for l in dict[j]:
#                                         totDists.append(Levenshtein.distance(k,l))
#                     #          pass
#                     '''
            
#         except UnicodeDecodeError:
#             pass
#             #print(dict)
# print(dict)
# l1,l2=[],[]
# for i in dict:
#     l1.append(i)
#     l2.append(dict[i])
# print(l1,l2)

#                 #save the results
#                 #then we reset array

# #print(countOfContstructs, countOfNonContstructs)
# #print(totalOverMethods)
# #fig = plt.figure(figsize =(10, 7)
# # Creating plot

# #fig, axs = plt.subplots(1, 2)
# #fig = plt.figure(figsize =(10, 7))
# #print(totalOverMethods/totalMethods)
# # Creating plot
# #plt.hist(otherList)
# #plt.title('Percentage of Methods that are Currently Overloaded in Top Repositories')
# #plt.xlabel('Average LOC at Different Points in LifeSpan')
# #plt.ylabel('Percentage of overloaded methods')
# print (n)
 
# # show plot
# #plt.show()

# #plt.savefig('C:\\Users\\willi\\Summer-Work21\\dists')

 

# # We can set the number of bins with the *bins* keyword argumen
# #plt.ylabel('Probability')
# #plt.xlabel('Data')