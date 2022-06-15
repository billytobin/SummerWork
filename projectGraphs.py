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

numOfVersions = int(sys.argv[1])

project_list = os.listdir('C:\\Users\\willi\\Summer-Work21\\Results\\Results5')


for repo in project_list:


    overloadedCount = []
    x_axis = []
    y_axis = []

    if path.exists("C:\\Users\\willi\\Summer-Work21\\Results\\Results5\\"+repo+"\\Result0.txt"):
        

        f = open("C:\\Users\\willi\\Summer-Work21\\Results\\Results5\\"+repo+"\\Result0.txt")
        #print(repo)

        data = json.load(f)


        contribCount =  data["Project Wide Statistics"]["Number of Contributors"]
        overloadedCount.insert(0, data["Project Wide Statistics"]["Total Overloaded Methods"])
        y_axis.insert(0, data["Project Wide Statistics"]['percentage of overloaded'])
        x_axis.insert(0, data["Project Wide Statistics"]['Commit Number'])
    for i in range(1, numOfVersions):

    
        if path.exists("C:\\Users\\willi\\Summer-Work21\\Results\\Results5\\"+repo+"\\Result"+str(i)+".txt"):
            f = open("C:\\Users\\willi\\Summer-Work21\\Results\\Results5\\"+repo+"\\Result"+str(i)+".txt")
            data = json.load(f)
            overloadedCount.insert(0,data["Project Wide Statistics"]["Total Overloaded Methods"])
            y_axis.insert(0, data["Project Wide Statistics"]['percentage of overloaded'])
            x_axis.insert(0, data["Project Wide Statistics"]['Commit Number'])
    deltaList = []
    for j in range(0, len(overloadedCount)-1):
        deltaList.append(overloadedCount[j+1] - overloadedCount[j])
       
    if x_axis and y_axis:
        fig = plt.figure()        
        xaxis = x_axis[1:]
        newX = []
        for i in xaxis:
            newX.append(str(i))
        plt.bar(newX, deltaList)
        plt.xlabel('Commits Ago (oldest to newest)')
        plt.ylabel('Num of Overloaded Methods Added')
        plt.title('Delta Graph for Different Versions of '+ repo)
        plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs4\\'+repo+'Delta.png')
        plt.clf()
        plt.plot(x_axis, y_axis)
        plt.xlim(max(x_axis),min(x_axis))

        plt.xlabel('Commits ago -- (Older to Newer)')  # Add an x-label to the axes.
        plt.ylabel('Percentage of Overloaded Methods')
        plt.title(repo)  # Add a title to the axes.
        #plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Results1.2\\RxJava\\graph.png')
        dir = "C:\\Users\\willi\\Summer-Work21\\Results\\Graphs4\\" +repo
        if not os.path.exists(dir):
            os.mkdir(dir)
        plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs4\\'+repo+'\\Percent.png')

        plt.clf()
        plt.plot(x_axis, overloadedCount)
        plt.xlim(max(x_axis),min(x_axis))

        plt.xlabel('Commits ago -- (Older to Newer)')  # Add an x-label to the axes.
        plt.ylabel('Number of Overloaded Methods')
        plt.title(repo)  # Add a title to the axes.
        #plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Results1.2\\RxJava\\graph.png')
        plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs4\\'+repo+'Total.png')