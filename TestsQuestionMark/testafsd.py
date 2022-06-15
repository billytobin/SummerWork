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

#numOfVersions = int(sys.argv[1])

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

#time.sleep(10)


count = 0
project_list = []
url_list = []

for j in temp_Repos[25:]:
    t = g.search_repositories(query=f"repo:{j}")
    i = t[0]
    print(i, i.stargazers_count)