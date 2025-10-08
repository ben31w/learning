"""
This program uses Plotly to create a bar graph displaying the number of comments
on each of the 30 articles on the current front page of Hacker News (a website 
where people discuss articles about programming and technology).
"""
from operator import itemgetter

import requests

from plotly.graph_objs import Bar, Layout, Figure
from plotly import offline

# Make an API call, and store the response.
#  This API call returns a list containing the IDs of 500 current 'top stories'
#  on Hacker News.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
submission_ids = r.json()

# Build dictionaries for each submission.
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    #  Each API call returns a dictionary containing info about each article.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    response_dict = r.json()

    # Build a dictionary.
    submission_dict = {
        'title': response_dict['title'],
        'link': f"http://news.ycombinator.com/item?id={submission_id}",
    }
    try:
        submission_dict['comments'] = response_dict['descendants']
    except KeyError:
        submission_dict['comments'] = 0

    submission_dicts.append(submission_dict)

# Sort the submissions by the number of comments.
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
    reverse=True)

# Store data from each submission in lists.
links, nums_comments = [], []
for submission_dict in submission_dicts:
    name = submission_dict['title']
    url = submission_dict['link']
    links.append(f"<a href='{url}'>{name}</a>")

    nums_comments.append(submission_dict['comments'])

# Plot the submissions.
data = [
    Bar(
        x=[link for link in links],
        y=[num for num in nums_comments],
        marker=dict(
            color='orange', 
            line=dict(width=1.5, color='rgb(25, 25, 25)')
        ),
        opacity=0.6,
        textfont=dict(color='white')
    )
]
layout = Layout(
    title='Current Top 30 Articles on Hacker News',
    titlefont=dict(size=28),
    xaxis=dict(title='Article Name', titlefont=dict(size=16)),
    yaxis=dict(title='Number of Comments', titlefont=dict(size=16))
)

fig = Figure(data=data, layout=layout)
offline.plot(fig, filename='html_files/top_hacker_news_articles.html')