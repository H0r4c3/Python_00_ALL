'https://docs.python-requests.org/en/latest/'

'''
Requests is an elegant and simple HTTP library for Python, built for human beings.
Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add 
query strings to your URLs, or to form-encode your POST data. 
Keep-alive and HTTP connection pooling are 100% automatic, thanks to urllib3.
'''

import requests

r = requests.get('https://api.github.com/events')

print(r.text)
print(r.status_code)



# Passing Parameters In URLs
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)




url = r'https://py.checkio.org/user/H0r4c3/'
r = requests.get(url)

print(r.headers)