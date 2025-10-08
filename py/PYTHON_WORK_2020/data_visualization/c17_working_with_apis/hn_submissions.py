"""
This program prints info about the 30 articles on the current front page of 
Hacker News (a website where people discuss articles about programming and 
technology) when it is run.
"""
from operator import itemgetter

import requests

# Make an API call, and store the response.
#  This API call returns a list containing the IDs of 500 current 'top stories'
#  on Hacker News.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process info about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    #  Each API call returns a dictionary containing info about each article.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'link': f"http://news.ycombinator.com/item?id={submission_id}",
    }
    try:
        submission_dict['comments'] = response_dict['descendants']
    except KeyError:
        submission_dict['comments'] = 0

    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
    reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['link']}")
    print(f"Comments: {submission_dict['comments']}")