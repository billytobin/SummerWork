from github import Github
from time import sleep

access_token = "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"
reqStars = 30000

g = Github(access_token)

current_user = g.get_user()

##print(current_user.name)
#print(current_user.bio)

#java_repos = g.search_repositories(query=f"language:java, stars:44000..45000")
java_repos = g.search_repositories(query=f"language:java, stars:11000..11950")

count = 0

for repo in java_repos:
    print(repo.name, repo.stargazers_count, repo.size)
    #count += 1
    #print(repo.html_url)
    
print(f"There are {java_repos.totalCount} Java repositories with more than x stars.")