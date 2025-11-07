'''
Created on Dec 22, 2020

@author: Horace.000
'''
'https://learning.oreilly.com/library/view/hands-on-web-scraping/9781789533392/dad77d6c-5afa-4e5e-a179-e3121091ec02.xhtml'
'''
Requests is an elegant and simple HTTP library for Python
More information on requests can be found at http://docs.python-requests.org/en/master/.
Gets rid of manual actions, like encoding form values
API-based link headers
The requests library also supports HTTP requests such as PUT, POST, DELETE, HEAD, and OPTIONS using the put(), post(), delete(), head(), and options() methods, respectively.
'''

import requests

link="http://www.python-requests.org"
r = requests.get(link)

print(r.url) #URL of response object

print(r.status_code) #status code

print(r.headers) #response headers with information about server, date..

print(r.headers['Content-Type']) #specific header Content-Type

print(r.request.headers)  #Request headers

print(r.encoding)  #response encoding

print(r.content[0:400])  #return 400 bytes characters

print(r.text[0:400])  #returns a sub string that is 400 string character from response

link2 = "https://feeds.citibikenyc.com/stations/stations.json"
response2 = requests.get(link2).json()
for i in range(10): #read 10 stationName from JSON response.
    print('Station ', response2['stationBeanList'][i]['stationName'])
    
    
# We will be using the requests Python library to implement common HTTP methods (GET and POST) that execute the HTTP-based communication scenario we listed previously.
"It's always beneficial to learn and detect the request and response sequences that are made with URLs through the browser and the available DevTools."

link="http://www.test-domain.com"
queries= {'id':'123456','display':'yes'}
addedheaders={'user-agent':''} #request made with parameters and headers
r = requests.get(link, params=queries, headers=addedheaders) 
print(r.url)

pageUrl="http://httpbin.org/forms/post"
postUrl="http://httpbin.org/post"
params = {'custname':'Mr. ABC','custtel':'','custemail':'abc@somedomain.com','size':'small','topping':['cheese','mushroom'],'delivery':'13:00','comments':'None'}
headers={ 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Content-Type':'application/x-www-form-urlencoded','Referer':pageUrl}
# making POST request to postUrl with params and request headers, response will be read as JSON
response = requests.post(postUrl,data=params,headers=headers).json()
print(response)

