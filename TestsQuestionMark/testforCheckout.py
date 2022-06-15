import json
import matplotlib.pyplot as plt
import numpy as np

from github import Github
import subprocess
import shutil
import os
from os import path
import sys

numOfVersions = int(5)

#reqStars =30000
access_token = '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'

g = Github(access_token)

java_repos = g.search_repositories(query=f"language:java, stars:30000..40001")

count = 0
project_list = []
url_list = []

for i in java_repos:
    numOfCommits = i.get_commits().totalCount
    diff = numOfCommits // numOfVersions
    list = []
    for j in range(1, numOfVersions):
        list.append(j*diff)

    #dir = "C:\\Users\\willi\\Summer-Work21\\Results\\Results1.5\\" +i.name
    #if not os.path.exists(dir):
    #    os.mkdir(dir)



    #cmd = 'git clone ' + i.html_url
    #pipe = subprocess.Popen(cmd, cwd='C:\\Users\\willi\\Summer-Work21\\finalRepos')
    #pipe.wait()
    #getting num of contributors
    #i = i.get_commit(i.get_commits()[200].sha)
    i = i.commit(i.get_commits()[200].sha)
    print(i)
    # print(i.get_contributors().totalCount)

