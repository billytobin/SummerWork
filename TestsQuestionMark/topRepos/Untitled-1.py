
from github import Github
import subprocess
import shutil

reqStars =30000
access_token = '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'

g = Github(access_token)

java_repos = g.search_repositories(query=f"language:java, stars:>={reqStars}")

count = 0
project_list = []
url_list = []

for repo in java_repos:
    count += 1
    project_list.append(repo.name)
    url_list.append(repo.html_url)

for url in url_list:
    
    cmd = 'git clone ' + url
    pipe = subprocess.Popen(cmd, cwd='C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\topRepos')
    pipe.wait()

for name in project_list:
    cmd = 'java -jar ck-0.6.5-SNAPSHOT-jar-with-dependencies.jar C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\topRepos\\'+ name + ' False 0 False'
    pipe = subprocess.Popen(cmd, cwd='C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\ck\\target')
    print("starting "+name)
    pipe.wait()
    print("done anaylzing "+name)
    shutil.move("C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\ck\\target\\output.txt", "C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\newRepos\\"+name+"result.txt")
    print("done moving "+name)
