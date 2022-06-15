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

numOfVersions = int(sys.argv[1])
moreCount = 0
lessCount = 0
project_list = os.listdir('C:\\Users\\willi\\Summer-Work21\\Results\\Results5')

bigDeltaList = []

contribList = []
percentList = []
for repo in project_list:


    overloadedCount = []
    x_axis = []
    y_axis = []

    if path.exists("C:\\Users\\willi\\Summer-Work21\\Results\\Results5\\"+repo+"\\Result0.txt"):
        

        f = open("C:\\Users\\willi\\Summer-Work21\\Results\\Results5\\"+repo+"\\Result0.txt")
        #print(repo)

        data = json.load(f)
        if repo != "CircleImageView":
            contribList.insert(0, data["Project Wide Statistics"]["Number of Contributors"])
            percentList.insert(0, data["Project Wide Statistics"]['percentage of overloaded'])
        #overloadedCount.insert(0, data["Project Wide Statistics"]["Total Overloaded Methods"])
            overloadedCount.insert(0, data["Project Wide Statistics"]['percentage of overloaded'])
        y_axis.insert(0, data["Project Wide Statistics"]['percentage of overloaded'])
        x_axis.insert(0, data["Project Wide Statistics"]['Commit Number'])
    for i in range(1, numOfVersions):

    
        if path.exists("C:\\Users\\willi\\Summer-Work21\\Results\\Results5\\"+repo+"\\Result"+str(i)+".txt"):
            f = open("C:\\Users\\willi\\Summer-Work21\\Results\\Results5\\"+repo+"\\Result"+str(i)+".txt")
            data = json.load(f)
            #overloadedCount.insert(0,data["Project Wide Statistics"]["Total Overloaded Methods"])
            if repo != "CircleImageView":
                overloadedCount.insert(0,data["Project Wide Statistics"]['percentage of overloaded'])
            y_axis.insert(0, data["Project Wide Statistics"]['percentage of overloaded'])
            x_axis.insert(0, data["Project Wide Statistics"]['Commit Number'])

    if y_axis[numOfVersions-1]-y_axis[0] >= 0:
        moreCount+= 1
    else:
        lessCount +=1

    #if repo != "CircleImageView":
     #   percentList[0] -= y_axis[7]   

    for j in range(0, len(overloadedCount)):
        if overloadedCount[j] == None:
            overloadedCount[j] = 0.0
    deltaList = []
    for j in range(0, len(overloadedCount)-1):
        deltaList.append(overloadedCount[j+1] - overloadedCount[j])
    #print(repo + str(deltaList))
    if bigDeltaList == []:
        for i in deltaList:
            bigDeltaList.append(i/ len(project_list))
    else:
        for i in range(0, len(deltaList)):
            bigDeltaList[i] += (abs(deltaList[i])/ len(project_list))
       
    
            
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

print(moreCount, lessCount)
fig = plt.figure() 
plt.clf()
#print((contribList), (percentList))
xs, ys = zip(*sorted(zip(contribList, percentList)))
plt.scatter(xs, ys)
#plt.plot(contribList, percentList)
plt.title('Percentage of Overloaded Methods For Each Repository')
plt.xlabel('Number of Contributors')
plt.ylabel('Percent Change of Methods that are Overloaded')
plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs4\\ContribVsPercent3.png')

plt.clf()
       
#plt.bar([1,2,3,4,5,6,7,8,9,10,11,12,13,14], bigDeltaList)
#plt.title('Change in Overloaded Methods Across Many Projects')
#plt.xlabel('Stage in Lifespan (Older to Newer)')
#plt.ylabel('Num of Overloaded Methods Taken/Added')
#plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs4\\genTest.png')


plt.close(fig)