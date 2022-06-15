
from github import Github
import subprocess
import shutil
import os
import matplotlib

reqStars =30000
access_token = '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'

g = Github(access_token)

java_repos = g.search_repositories(query=f"language:java, stars:>={reqStars}")

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
numOfCommits = java_repos[8].get_commits().totalCount

quartile = numOfCommits//4 
half = numOfCommits//2
upperQuartile = (numOfCommits//4) * 3

list = [quartile, half, upperQuartile]
print(list)

cmd = 'git clone ' + java_repos[8].html_url
pipe = subprocess.Popen(cmd, cwd='C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\repeatRepos')
pipe.wait()
#pipe = subprocess.Popen('git log', cwd='C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\repeatRepos\\'+java_repos[8].name)

#os.rmdir("C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\ck\\target\\output.txt")

i = 1
for value in list:
    pipe = subprocess.Popen('git show ' + java_repos[8].get_commits()[value].sha, cwd='C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\repeatRepos\\'+java_repos[8].name)

pipe = subprocess.Popen('git show ' + java_repos[8].get_commits()[100].sha, cwd='C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\repeatRepos\\'+java_repos[8].name)