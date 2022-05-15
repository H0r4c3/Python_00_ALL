'https://app.pluralsight.com/course-player?clipId=1e061ac5-f5f7-4dd1-8316-563f61a99c82'

import requests

URL = 'http://api.open-notify.org/astros.json'

response = requests.get(URL)

my_json = response.json() # dictionary

for item in my_json.get('people'):
    print(item.get('name'))