'''
ChatGPT

https://chat.openai.com/

Here's a Python program that uses the requests library to fetch the headers of a website and extract the server time:


This program prompts the user to enter the URL of the website they want to check. 
It then sends a HEAD request to the website using the requests library and checks if the response headers contain the "Date" header. 
If the header is found, the program prints the server time in UTC format. If the header is not found, the program prints an error message.

Note that some websites may not include the "Date" header in their responses, in which case this program will not be able to find the server time.

https://py.checkio.org/
'''


import requests

url = input("Enter the URL of the website: ")
response = requests.head(url)

if "Date" in response.headers:
    server_time = response.headers["Date"]
    print("Server time of", url, "is", server_time)
else:
    print("Could not find server time.")