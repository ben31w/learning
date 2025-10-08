"""
This program uses Plotly to create a bar graph displaying the most popular 
Python projects on Github. This version of the program uses classes from 
plotly.graph_objs instead of dictionaries, and it uses dict() functions when
defining dictionary attributes. 
"""
from datetime import date

import requests

from plotly.graph_objs import Bar, Layout, Figure
from plotly import offline

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application.vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process results.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br / >{description}"
    labels.append(label)

# Make visualization.
data = [
    Bar(
        x=repo_links, 
        y=stars, 
        hovertext=labels, 
        marker=dict(
            color='rgb(60, 100, 150)',
            line=dict(
                width=1.5,
                color='rgb(25, 25, 25)'
            )
        ),
        opacity=0.6
    )
]
layout = Layout(
    title=f"Most-Starred Python Projects on Github ({date.today()})",
    titlefont=dict(size=28),
    xaxis=dict(
        title='Repository',
        titlefont=dict(size=16)
    ),
    yaxis=dict(
        title='Stars',
        titlefont=dict(size=16)
    )
)

fig = Figure(
    data=data,
    layout=layout
)
offline.plot(fig, filename='python_repos.html')