import requests
import requests_cache
import json
import time
from IPython.core.display import clear_output
from warnings import warn
import pandas as pd

requests_cache.install_cache()

API_KEY = '3a17667e0fcb3cda92a899aa2cb4f43e'
USER_AGENT = 'Dataquest'


def lastfm_get(payload):
    headers = {'user-agent': USER_AGENT}
    url = 'http://ws.audioscrobbler.com/2.0/'

    payload['api_key'] = API_KEY
    payload['format'] = 'json'

    response = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
    return response


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


r = lastfm_get({
    'method': 'chart.gettopartists',
})


results = []
page = 1
total_pages = 99999 # this is just a dummy number so the loop starts

while page <= total_pages:
    payload = {
        'method': 'chart.gettopartists',
        'limit': 500,
        'page': page
    }

    print("Requesting page {}/{}".format(page, total_pages))

    clear_output(wait=True)

    response = lastfm_get(payload)

    if response.status_code != 200:
        print(response.text)
        break

    page = int(response.json()['artists']['@attr']['page'])
    total_pages = int(response.json()['artists']['@attr']['totalPages'])

    results.append(response)

    if not getattr(response, 'from_cache', False):
        time.sleep(0.25)
        page += 1

r0 = results[0]
r0_json = r0.json()
r0_artists = r0_json['artists']['artist']
r0_df = pd.DataFrame(r0_artists)
r0_df.head()

# Concat each json object in frames for all artists
frames = [pd.DataFrame(r.json())['artists']['artist'] for r in results]
artists = pd.concat(frames)
artists.head()

# Useless image data
artists = artists.drop('image, axis=1')
artists.head()

# Summary of the table
artists.info()
artists.describe()

# remove duplicates and fix indices
artists = artists.drop_duplicates().reset_index(drop=True)
artists.describe()



