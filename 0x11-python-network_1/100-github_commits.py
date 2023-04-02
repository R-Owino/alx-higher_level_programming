#!/usr/bin/python3
"""
lists the 10 most recent commits on a given GitHub repository
using Github API
"""
import sys
import requests


if __name__ == "__main__":

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)

    commits = response.json()[:10]  # get first 10 commits
    try:
        for commit in commits:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")
    except IndexError:
        pass
