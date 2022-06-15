#Billy Tobin
#Cloning, analyzing, and making x projects
#
#
import json
import matplotlib.pyplot as plt
import numpy as np

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
project_list = os.listdir('C:\\Users\\willi\\Summer-Work21\\Results\\Results5')

bigDeltaList = []
TimesOverloadedCount = []
TimesOverloadedCount1 = []
contribList = []
otherList = []


isStaticCount = [0] * numOfVersions
isnotStaticCount = [0] * numOfVersions

percentList = []
totalOverMethods = [0] * numOfVersions
countOfContstructs = [0] * numOfVersions
countOfNonContstructs = [0] * numOfVersions
totalList= [0]*2

#locCount = [0]*(len(project_list)-1)
locCount = []

upCount= [0]*(numOfVersions-1)
downCount = [0]*(numOfVersions-1)

n = (-1)

new = {}

def addToDict(method, dict, num):
    if method in dict:
        dict[method] += num
    else:
        dict[method]= num

def getName(method):
    index = method.rfind('.')
    return method[index+1:]

def getDict(repo, i):

    dicti = {}

    if path.exists("C:\\Users\\willi\\Summer-Work21\\Results\\Results5\\"+repo+"\\Result"+str(i)+".txt"):
            
            f = open("C:\\Users\\willi\\Summer-Work21\\Results\\Results5\\"+repo+"\\Result"+str(i)+".txt")
            data = json.load(f)
            
            
            for className in data:
                
                if className != "Project Wide Statistics":
                   # totalOverMethods[i] += data[className]['Class Wide Statistics']["numberOfMethods\t"]
    

                    #locCount[i] += (data[className]['Class Wide Statistics']["loc"] / len(project_list))
                    
                    for method in data[className]:
                        if (method != 'Class Wide Statistics') and (method != 'Num Of Overloaded Methods'):
                            totalOverMethods[i] += data[className][method]['Times Overloaded']
                            #print(method, data[className][method]['Times Overloaded'])
                        #print(method)

                            dicti[className + "." + method] = data[className][method]['Times Overloaded']

    return dicti

upDict = {}
downDict = {}
totalChangeDict = {}

for repo in range(0,len(project_list)):
    #len(project_list)

    new = getDict(project_list[repo], 0)

    #print ('\n')

    for i in range(1, numOfVersions):
        #numOfVersions

        changes = {}

        old = getDict(project_list[repo], i)

        #print ('\n\n')

        #print(project_list[repo])

        temp = old.copy()

        for method in new:
            if method in temp:
                #for below line, changes[method]will be pos if the method increased in num of times overload, neg if vice versa
                changes[method] = new[method] - temp[method]

                #print(method, new[method], temp[method])
                
                temp.pop(method)
                #new.pop(method)
            else:
                #print("NEW:", method, new[method])
                #method was completely added of in terms of overloadedness
                changes[method]= new[method]
        
        for method in temp:
            #print(method, temp[method])
            changes[method]= -1*temp[method] 

        new = old

        t = True

        """ names = {}
        for method in changes:
            methodName = getName(method)

            names[methodName] = changes[method] """
    
        for method in changes:
            methodName= getName(method)
            
            if t:
                #print(method + ":"+ str(changes[method]))
                t = False
            if changes[method] >= 0:
                upCount[i-1] += changes[method]
                addToDict(methodName, upDict, changes[method])
            else:
                addToDict(methodName, downDict, changes[method])
                downCount[i-1] += changes[method]
            addToDict(methodName, totalChangeDict, changes[method])



print(upCount)
print(downCount)

#print(upDict)
#print("\n\n------------------------------------------\n\n")
#print(downDict)
#print("\n\n------------------------------------------\n\n")
#print(totalChangeDict)

def getHighest(dict, numHighest):
    retDict = {}
    for i in range(numHighest):
        max_key = max(dict, key=dict.get)
        retDict[max_key] = dict[max_key]
        dict.pop(max_key)

    return retDict

def getLowest(dict, numHighest):
    retDict = {}
    for i in range(numHighest):
        max_key = min(dict, key=dict.get)
        retDict[max_key] = dict[max_key]
        dict.pop(max_key)

    return retDict

print(getHighest(upDict, 50))
print(getLowest(downDict, 50))
print(getHighest(totalChangeDict, 50))

lyst =[]
for i in range(len(totalOverMethods)-1):
    lyst.append(totalOverMethods[i]- totalOverMethods[i+1])

l1,l2 = [],[]



for i in range(len(downCount)):
    downCount[i] = abs(downCount[i])/ (numOfVersions-1)
    #print("hello")
    #l1.append(i)
    #l2.append(abs(downDict[i]))


print(downCount)
fig = plt.figure()
commit = [14,13,12,11,10,9,8,7,6,5,4,3,2,1]
plt.bar(commit, (downCount))
plt.xlabel('Commits Ago (oldest to newest)')
plt.xlim(max(commit),min(commit))
plt.ylabel('Number of Overloaded Methods Lost')
plt.title('Average Loss in Overloaded Methods')
plt.show()

#print(lyst)
#print(totalOverMethods)


    
        

            
                    
   