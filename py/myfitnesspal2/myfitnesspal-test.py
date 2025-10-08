"""
Request some test data from MyFitnessPal.

2024.03.30
"""

import requests

url = "https://api.myfitnesspal.com/v2/diary"
headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer',      # Needs an API token
    'mfp-client-id': ''             # Client id associated with the token.
}

r = requests.get(url, headers=headers)
print(r)