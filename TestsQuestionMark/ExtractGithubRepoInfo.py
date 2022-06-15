
from github import Github
import pandas as pd

reqStars = 40000
access_token = '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'

g = Github(access_token)

java_repos = g.search_repositories(query=f"language:java, stars:>={reqStars}")

count = 0
project_list = []

for repo in java_repos:
    #print(repo.name, repo.size)
    count += 1
    project_list.append(repo.full_name)


def extract_project_info():
    df_project = pd.DataFrame()

    d = 0
    for project in project_list:
        g = Github(access_token)
        repo = g.get_repo(project)
        d = 0
        #print(repo.get_contributors())
        for c in repo.get_contributors():
            d += 1
        print(d, repo.name)

        df_project = df_project.append({
            'Project_ID': repo.id,
            'Name': repo.name,
            'Full_name': repo.full_name,
            'HTML_Link': repo.html_url,
            'Stars': repo.stargazers_count,
            'Watchers': repo.subscribers_count,
            'Contributors': repo.contributors_url
        }, ignore_index=True) 

    #df_project.to_csv('../Dataset/project_dataset.csv', sep=',', encoding='utf-8', index=True)

    #print(df_project)

extract_project_info()