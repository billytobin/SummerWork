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

access_token = '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'

g = Github(access_token)

java_repos = g.search_repositories(query=f"language:java, stars:50000..100000")

project_list=[]


for repo in java_repos:
    project_list.append(repo.name)

for repo in project_list:

    overloadedlist=[]
    x_axis = []
    y_axis = []

    if path.exists("C:\\Users\\willi\\Summer-Work21\\Results\\Results1.2\\"+repo+"\\CurrentResult.txt"):
        

        f = open("C:\\Users\\willi\\Summer-Work21\\Results\\Results1.2\\"+repo+"\\CurrentResult.txt")
        print(repo)

        data = json.load(f)

        overloadedlist.append(data["Project Wide Statistics"]["Total Overloaded Methods"])
        y_axis.append(data["Project Wide Statistics"]['percentage of overloaded'])
        x_axis.append(data["Project Wide Statistics"]['Commit Number'])

    for i in range(1,4):
        if path.exists("C:\\Users\\willi\\Summer-Work21\\Results\\Results1.2\\"+repo+"\\Result"+str(i)+".txt"):
            f = open("C:\\Users\\willi\\Summer-Work21\\Results\\Results1.2\\"+repo+"\\Result"+str(i)+".txt")
            data = json.load(f)

            overloadedlist.append(data["Project Wide Statistics"]["Total Overloaded Methods"])
            y_axis.append(data["Project Wide Statistics"]['percentage of overloaded'])
            x_axis.append(data["Project Wide Statistics"]['Commit Number'])

        #print(data["Project Wide Statistics"]['percentage of overloaded'])
        




    #fig, ax = plt.subplots()
    #y_axis.reverse()
    print(overloadedlist)
    #print(y_axis)
    if x_axis and y_axis:
        plt.plot(x_axis, y_axis)
        plt.xlim(max(x_axis),min(x_axis))

        plt.xlabel('Commits ago -- (Older to Newer)')  # Add an x-label to the axes.
        plt.ylabel('Percentage of Overloaded Methods')
        plt.title(repo)  # Add a title to the axes.
        #plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Results1.2\\RxJava\\graph.png')
        plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs\\'+repo+'.png')
        plt.clf()
    #plt.show()