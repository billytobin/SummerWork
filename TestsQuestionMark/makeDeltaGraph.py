#Billy Tobin
#Making all graphs for projects we know
#NOT CLONING OR ANALYZING
#PreReq: 4 different analyses must be done on the diff repos
import json
import matplotlib.pyplot as plt
import numpy as np


from github import Github
import subprocess
import shutil
from os import path
import sys

numOfVersions = int(sys.argv[1])

access_token = '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'

g = Github(access_token)

java_repos = g.search_repositories(query=f"language:java, stars:5630..5717")

for i in java_repos:
    numOfCommits = i.get_commits().totalCount
    diff = numOfCommits // numOfVersions
    list = []
    for j in range(1, numOfVersions):
        list.append(j*diff)

project_list=[]

for repo in java_repos:
    project_list.append(repo.name)

for repo in project_list:

    overloadedCount = []
    x_axis = []
    y_axis = []

    if path.exists("C:\\Users\\willi\\Summer-Work21\\Results\\Results1.3\\"+repo+"\\CurrentResult.txt"):
        

        f = open("C:\\Users\\willi\\Summer-Work21\\Results\\Results1.3\\"+repo+"\\CurrentResult.txt")
        print(repo)

        data = json.load(f)

        overloadedCount.insert(0, data["Project Wide Statistics"]["Total Overloaded Methods"])
        y_axis.insert(0, data["Project Wide Statistics"]['percentage of overloaded'])
        x_axis.insert(0, data["Project Wide Statistics"]['Commit Number'])

    for i in range(1, numOfVersions):
        if path.exists("C:\\Users\\willi\\Summer-Work21\\Results\\Results1.3\\"+repo+"\\Result"+str(i)+".txt"):
            f = open("C:\\Users\\willi\\Summer-Work21\\Results\\Results1.3\\"+repo+"\\Result"+str(i)+".txt")
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
        plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs2\\'+repo+'Delta.png')
        plt.clf()
        plt.plot(x_axis, y_axis)
        plt.xlim(max(x_axis),min(x_axis))

        plt.xlabel('Commits ago -- (Older to Newer)')  # Add an x-label to the axes.
        plt.ylabel('Percentage of Overloaded Methods')
        plt.title(repo)  # Add a title to the axes.
        #plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Results1.2\\RxJava\\graph.png')
        plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs2\\'+repo+'Percent.png')

        plt.clf()
        plt.plot(x_axis, overloadedCount)
        plt.xlim(max(x_axis),min(x_axis))

        plt.xlabel('Commits ago -- (Older to Newer)')  # Add an x-label to the axes.
        plt.ylabel('Number of Overloaded Methods')
        plt.title(repo)  # Add a title to the axes.
        #plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Results1.2\\RxJava\\graph.png')
        plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs2\\'+repo+'Total.png')