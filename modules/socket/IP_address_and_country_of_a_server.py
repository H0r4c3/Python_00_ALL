'''
ChatGPT:

Here's a Python program that uses the socket and geocoder libraries to find the IP address and country of a server:

This program prompts the user to enter the URL of the website they want to check. 
It then uses the socket library to resolve the hostname to an IP address, and the geocoder library to find the country of that IP address.

If the IP address is successfully resolved, the program prints the IP address of the server. 
It then uses geocoder.ip() method to obtain the country of the IP address, and prints it if it is available. 
If the country information is not available, the program prints an error message.

Note that some servers may not have a specific country associated with their IP address, or the country information may not be available through the geocoder library.

py.checkio.org
'''

import socket
import geocoder

url = input("Enter the URL of the website: ")

try:
    ip_address = socket.gethostbyname(url)
    print("IP address of", url, "is", ip_address)

    location = geocoder.ip(ip_address)
    if location.country:
        print("Country of", ip_address, "is", location.country)
    else:
        print("Could not find country information.")
except socket.gaierror:
    print("Could not resolve hostname.")