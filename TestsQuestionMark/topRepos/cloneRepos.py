
from github import Github
import subprocess

reqStars = 25000
access_token = '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'

g = Github(access_token)

java_repos = g.search_repositories(query=f"language:java, stars:>={reqStars}")

count = 0
project_list = []

for repo in java_repos:
    count += 1
    project_list.append(repo.html_url)

for url in project_list:
    cmd = 'git clone ' + url
    pipe = subprocess.Popen(cmd, shell=True)
    pipe.wait()

