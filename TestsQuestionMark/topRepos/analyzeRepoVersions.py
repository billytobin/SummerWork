<<<<<<< HEAD

from github import Github
import subprocess
import shutil
import os

reqStars =30000
access_token = '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'

g = Github(access_token)

java_repos = g.search_repositories(query=f"language:java, stars:10000..20000")

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

    list = [quartile, half, upperQuartile]
    print(list)

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
    for value in list:
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
=======

from github import Github
import subprocess
import shutil
import os

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

dir = "C:\\Users\\willi\\Summer-Work21\\Results\\Results1.2\\" +java_repos[8].name
if not os.path.exists(dir):
    os.mkdir(dir)



cmd = 'git clone ' + java_repos[8].html_url
pipe = subprocess.Popen(cmd, cwd='C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\repeatRepos')
pipe.wait()
cmd = 'java -jar ck-0.6.5-SNAPSHOT-jar-with-dependencies.jar C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\repeatRepos\\'+ java_repos[8].name + ' False 0 False 0'
pipe = subprocess.Popen(cmd, cwd='C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\ck\\target')
pipe.wait()

shutil.move("C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\ck\\target\\output.txt", "C:\\Users\\willi\\Summer-Work21\\Results\\Results1.2\\" +java_repos[8].name+"\\CurrentResult.txt")
#os.rmdir("C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\ck\\target\\output.txt")

i = 1
for value in list:
    pipe = subprocess.Popen('git checkout '+ java_repos[8].get_commits()[value].sha, cwd='C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\repeatRepos\\'+java_repos[8].name) 
#print("starting ")
    pipe.wait()
    cmd = 'java -jar ck-0.6.5-SNAPSHOT-jar-with-dependencies.jar C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\repeatRepos\\'+ java_repos[8].name + ' False 0 False ' + str(value)
    pipe = subprocess.Popen(cmd, cwd='C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\ck\\target')
    pipe.wait()
    print("done anaylzing")
    shutil.move("C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\ck\\target\\output.txt", "C:\\Users\\willi\\Summer-Work21\\Results\\Results1.2\\" +java_repos[8].name+"\\Result"+ str(i) +".txt")
    i += 1
    pipe.wait()
>>>>>>> a26c85de42929b3ee1e850969772e1a1d69ad8c9
