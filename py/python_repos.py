"""
Generate an API call to GitHub. Get a collection of all the Python repositories
currently hosted on GitHub. Then print the 30 most popular.

Updated: 2023.04.19
"""
import requests

# Make an API call to GitHub and store the response.
# GitHub is currently on the third version of its API, so we define headers for
# the API call that explicitly ask to use this version of the API.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")


# Store API response in JSON format (a giant dictionary).
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")


# Get information about the repositories.
# In this example, the JSON file has a key called 'items' whose value is a 
# list of 30 dictionaries, with each dictionary representing a popular Python repository.
repo_dicts = response_dict['items']

names = "\nNames of the most popular repositories: "
for i in range(len(repo_dicts)):
    repo_dict = repo_dicts[i]
    names += f"{repo_dict['name']}"
    if i != len(repo_dicts)-1:
        names += ", "
print(names)


# Print selected info about each repository.
print("\nSelected info about each repository:")
for i in range(len(repo_dicts)):
    print(f"\n[{i+1}]")
    repo_dict = repo_dicts[i]
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")