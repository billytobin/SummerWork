
from github import Github
import subprocess
import shutil

reqStars = 30000
access_token = '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'

g = Github(access_token)

java_repos = g.search_repositories(query=f"language:java, stars:>={reqStars}")

count = 0
project_list = []


for repo in java_repos:
    if (repo.name != 'java-design-patterns') and (repo.name != 'spring-boot'):
        
        count += 1
        project_list.append(repo.name)
        

for name in project_list:
    cmd = 'java -jar ck-0.6.5-SNAPSHOT-jar-with-dependencies.jar C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\topRepos\\'+ name + ' False 100000 False'
    pipe = subprocess.Popen(cmd, cwd='C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\ck\\target')
    print("starting "+name)
    pipe.wait()
    print("done anaylzing "+name)
    shutil.move("C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\ck\\target\\class.csv", "C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\newRepos\\"+name+"_class.csv")
    shutil.move("C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\ck\\target\\method.csv", "C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\newRepos\\"+ name+"_method.csv")
    print("done moving "+name)
