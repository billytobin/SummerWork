import json
import matplotlib.pyplot as plt
import numpy as np

from github import Github
import subprocess
import shutil
import os
from os import path

reqStars =30000
access_token = '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'

g = Github(access_token)

java_repos = g.search_repositories(query=f"language:java, stars:5000..7000")

count = 0
project_list = []
url_list = []

""" for repo in java_repos:
    count += 1
    print(repo.name, repo.get_commits().totalCount)
    project_list.append(repo.name)
    url_list.append(repo.html_url) """
    #n = repo.get_commits().totalCount // 2
    #print(repo.name + "at commit"+n)

for i in java_repos:
    numOfCommits = i.get_commits().totalCount

    quartile = numOfCommits//4 
    half = numOfCommits//2
    upperQuartile = (numOfCommits//4) * 3

    lst = [quartile, half, upperQuartile]
    #print(list)

    dir = "C:\\Users\\willi\\Summer-Work21\\Results\\Results1.2\\" +i.name
    if not os.path.exists(dir):
        os.mkdir(dir)



    cmd = 'git clone ' + i.html_url
    pipe = subprocess.Popen(cmd, cwd='C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\repeatRepos')
    pipe.wait()
    cmd = 'java -jar ck-0.6.5-SNAPSHOT-jar-with-dependencies.jar C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\repeatRepos\\'+ i.name + ' False 0 False 0 '+ i.html_url + " " + i.get_commits()[0].sha
    pipe = subprocess.Popen(cmd, cwd='C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\ck\\target')
    pipe.wait()

    shutil.move("C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\ck\\target\\output.txt", "C:\\Users\\willi\\Summer-Work21\\Results\\Results1.2\\" +i.name+"\\CurrentResult.txt")
    #os.rmdir("C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\ck\\target\\output.txt")

    j = 1
    for value in lst:
        pipe = subprocess.Popen('git checkout '+ i.get_commits()[value].sha, cwd='C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\repeatRepos\\'+i.name) 
        #print("starting ")
        pipe.wait()
        cmd = 'java -jar ck-0.6.5-SNAPSHOT-jar-with-dependencies.jar C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\repeatRepos\\'+ i.name + ' False 0 False ' + str(value) + " " + i.html_url + " " + i.get_commits()[value].sha
        pipe = subprocess.Popen(cmd, cwd='C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\ck\\target')
        pipe.wait()
        print("done anaylzing")
        shutil.move("C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\ck\\target\\output.txt", "C:\\Users\\willi\\Summer-Work21\\Results\\Results1.2\\" +i.name+"\\Result"+ str(j) +".txt")
        j += 1
        pipe.wait()

for repo in java_repos:
    project_list.append(repo.name)

for repo in project_list:

    x_axis = []
    y_axis = []

    if path.exists("C:\\Users\\willi\\Summer-Work21\\Results\\Results1.2\\"+repo+"\\CurrentResult.txt"):
        

        f = open("C:\\Users\\willi\\Summer-Work21\\Results\\Results1.2\\"+repo+"\\CurrentResult.txt")
        print(repo)

        data = json.load(f)

        y_axis.append(data["Project Wide Statistics"]['percentage of overloaded'])
        x_axis.append(data["Project Wide Statistics"]['Commit Number'])

    for i in range(1,4):
        if path.exists("C:\\Users\\willi\\Summer-Work21\\Results\\Results1.2\\"+repo+"\\Result"+str(i)+".txt"):
            f = open("C:\\Users\\willi\\Summer-Work21\\Results\\Results1.2\\"+repo+"\\Result"+str(i)+".txt")
            data = json.load(f)

            y_axis.append(data["Project Wide Statistics"]['percentage of overloaded'])
            x_axis.append(data["Project Wide Statistics"]['Commit Number'])

    if x_axis and y_axis:
        plt.plot(x_axis, y_axis)
        plt.xlim(max(x_axis),min(x_axis))

        plt.xlabel('Commits ago -- (Older to Newer)')  # Add an x-label to the axes.
        plt.ylabel('Percentage of Overloaded Methods')
        plt.title(repo)  # Add a title to the axes.
        #plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Results1.2\\RxJava\\graph.png')
        plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs\\'+repo+'.png')
        plt.clf()