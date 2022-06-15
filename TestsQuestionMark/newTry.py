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
import time

numOfVersions = int(sys.argv[1])

#reqStars =30000
access_token = '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'
#access_token = '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'

g = Github(access_token)



projectlst = os.listdir(os.getcwd() + '\\Results\\Results5')

#java_repos = g.search_repositories(query=f"language:java, stars:11300..11550")

temp_Repos=[]

for i in projectlst:
    f = open("C:\\Users\\willi\\Summer-Work21\\Results\\Results5\\"+i+"\\Result0.txt")
        #print(repo)
        #locCount.insert(0,0)
        

    data = json.load(f)
    temp = data["Project Wide Statistics"]["Project URL"].split('/')
    #print(temp)
    OwnerName = temp[-2]+ '/' + temp[-1]
    #print(OwnerName)
    temp_Repos.append(OwnerName)

print(temp_Repos)

time.sleep(10)


count = 0
project_list = []
url_list = []

for j in temp_Repos:
    t = g.search_repositories(query=f"repo:{j}")
    i = t[0]
    numOfCommits = i.get_commits().totalCount
    diff = numOfCommits // numOfVersions
    list = []
    for j in range(1, numOfVersions):
        list.append(j*diff)

    dir = "C:\\Users\\willi\\Summer-Work21\\Results\\CurrentAnalysis\\" +i.name
    if not os.path.exists(dir):
        os.mkdir(dir)



    cmd = 'git clone ' + i.html_url
    pipe = subprocess.Popen(cmd, cwd='C:\\Users\\willi\\Summer-Work21\\currentRepos')
    pipe.wait()
    #getting num of contributors
    count = i.get_contributors().totalCount
    time.sleep(100)

    cmd = 'java -jar ck-0.6.5-SNAPSHOT-jar-with-dependencies.jar C:\\Users\\willi\\Summer-Work21\\currentRepos\\'+ i.name + ' False 0 False 0 '+ i.html_url + " " + i.get_commits()[0].sha + " " + str(count)
    pipe = subprocess.Popen(cmd, cwd='C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\ck\\target')
    pipe.wait()

    shutil.move("C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\ck\\target\\output.txt", "C:\\Users\\willi\\Summer-Work21\\Results\\CurrentAnalysis\\" +i.name+"\\Result0.txt")
    #os.rmdir("C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\ck\\target\\output.txt")

'''
    j = 1
    for value in list:
        time.sleep(200)
        pipe = subprocess.Popen('git checkout '+ i.get_commits()[value].sha, cwd='C:\\Users\\willi\\Summer-Work21\\currentRepos\\'+i.name) 
        #print("starting ")
        pipe.wait()

        # implement count here as well


        cmd = 'java -jar ck-0.6.5-SNAPSHOT-jar-with-dependencies.jar C:\\Users\\willi\\Summer-Work21\\currentRepos\\'+ i.name + ' False 0 False ' + str(value) + " " + i.html_url + " " + i.get_commits()[value].sha + " 0"
        pipe = subprocess.Popen(cmd, cwd='C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\ck\\target')
        pipe.wait()
        #print("done anaylzing")
        shutil.move("C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\ck\\target\\output.txt", "C:\\Users\\willi\\Summer-Work21\\Results\\CurrentAnalysis\\" +i.name+"\\Result"+ str(j) +".txt")
        j += 1
        pipe.wait()
'''
""" 
# for repo in java_repos:
#     project_list.append(repo.name)

# for repo in project_list:

#     overloadedCount = []
#     x_axis = []
#     y_axis = []

#     if path.exists("C:\\Users\\willi\\Summer-Work21\\Results\\Results1.5\\"+repo+"\\Result0.txt"):
        

#         f = open("C:\\Users\\willi\\Summer-Work21\\Results\\Results1.5\\"+repo+"\\Result0.txt")
#         #print(repo)

#         data = json.load(f)

#         overloadedCount.insert(0, data["Project Wide Statistics"]["Total Overloaded Methods"])
#         y_axis.insert(0, data["Project Wide Statistics"]['percentage of overloaded'])
#         x_axis.insert(0, data["Project Wide Statistics"]['Commit Number'])

#     for i in range(1, numOfVersions):
#         if path.exists("C:\\Users\\willi\\Summer-Work21\\Results\\Results1.5\\"+repo+"\\Result"+str(i)+".txt"):
#             f = open("C:\\Users\\willi\\Summer-Work21\\Results\\Results1.5\\"+repo+"\\Result"+str(i)+".txt")
#             data = json.load(f)

#             overloadedCount.insert(0,data["Project Wide Statistics"]["Total Overloaded Methods"])
#             y_axis.insert(0, data["Project Wide Statistics"]['percentage of overloaded'])
#             x_axis.insert(0, data["Project Wide Statistics"]['Commit Number'])

#     deltaList = []
#     for j in range(0, len(overloadedCount)-1):
#         deltaList.append(overloadedCount[j+1] - overloadedCount[j])
        

#     if x_axis and y_axis:
#         fig = plt.figure()        
#         xaxis = x_axis[1:]
#         newX = []
#         for i in xaxis:
#             newX.append(str(i))
#         plt.bar(newX, deltaList)
#         plt.xlabel('Commits Ago (oldest to newest)')
#         plt.ylabel('Num of Overloaded Methods Added')
#         plt.title('Delta Graph for Different Versions of '+ repo)
#         plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs3\\'+repo+'Delta.png')
#         plt.clf()
#         plt.plot(x_axis, y_axis)
#         plt.xlim(max(x_axis),min(x_axis))

#         plt.xlabel('Commits ago -- (Older to Newer)')  # Add an x-label to the axes.
#         plt.ylabel('Percentage of Overloaded Methods')
#         plt.title(repo)  # Add a title to the axes.
#         #plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Results1.2\\RxJava\\graph.png')
#         plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs3\\'+repo+'Percent.png')

#         plt.clf()
#         plt.plot(x_axis, overloadedCount)
#         plt.xlim(max(x_axis),min(x_axis))

#         plt.xlabel('Commits ago -- (Older to Newer)')  # Add an x-label to the axes.
#         plt.ylabel('Number of Overloaded Methods')
#         plt.title(repo)  # Add a title to the axes.
#         #plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Results1.2\\RxJava\\graph.png')
#         plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Graphs3\\'+repo+'Total.png') """