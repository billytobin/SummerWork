#Billy Tobin
#Cloning, analyzing, and making x projects
#
#
import json
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
#C:\Users\willi\Summer-Work21\TestsQuestionMark\CurrentResults\results\btrace-master

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
totDists =[]
array = []
dists = []
#rint(Levenshtein.distance("hello", "hell"))
            #print(dict)
 

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



                #save the results
                #then we reset array

#print(countOfContstructs, countOfNonContstructs)
#print(totalOverMethods)
#fig = plt.figure(figsize =(10, 7))
f = open("demofile2.txt", "r") #tots
gf = open("demofile3.txt", "r") #dists
st =f.read()
sf = gf.read()
# Creating plot
dists = sf.split(',')
totDists = st.split(',')

#print (dists)

for i in dists:
        
        i = int(i)
        


totDists.pop(len(totDists)-1)

for i in totDists:
        i = int (i)


print(mean(dists))
print(median(dists))

print(mean(totDists))
print(median(totDists)) 

fig, axs = plt.subplots(1, 2)

# We can set the number of bins with the *bins* keyword argument.
plt.hist(dists, density=True, bins=10)  # density=False would make counts
axs[0].hist(dists, bins=10)
axs[1].hist(totDists, bins=10)
#plt.ylabel('Probability')
#plt.xlabel('Data')
 
# show plot
plt.show()
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