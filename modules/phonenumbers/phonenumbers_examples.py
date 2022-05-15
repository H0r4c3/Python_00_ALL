'https://pypi.org/project/phonenumbers/'
'https://www.geeksforgeeks.org/phonenumbers-module-in-python/'

'''
Phone-numbers is the package used to find the phone number location and service provider. 
You will need to install this package on the terminal using pip install phonenumbers syntax. 
The package takes the input number, parses it, and validates it. 
Some essential features of the package are finding the country name of the phone number issuer and service provider for the number and timezone of the phone.

Python is a very powerful language and also very rich in libraries. phonenumbers is one of the modules that provides numerous features like providing 
basic information of a phone number, validation of a phone number etc. 
Here, we will learn how to use phonenumbers module just by writing simple Python programs. This is a Python port of Google’s libphonenumber library.

'''

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

#number = input("Enter your phone number")
number = "+40723450294"
phone_number = phonenumbers.parse(number)

phoneNumber = phonenumbers.parse("+40723450294")
print(geocoder.description_for_number(phone_number, "en"))
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))
service_provide = phonenumbers.parse(number)
print(timezone.time_zones_for_number(service_provide))


# Program to convert input to phonenumber format
  
# Parsing String to Phone number
# Phone number format: (+Countrycode)xxxxxxxxxx
#phoneNumber = phonenumbers.parse("+919876543210")
phoneNumber = phonenumbers.parse("+40723450294")
  
# This will print the phone number and it's basic details.
print(phoneNumber)


# Program to get timezone a phone number

# Parsing String to Phone number
phoneNumber = phonenumbers.parse("+40723450294")
  
# Pass the parsed phone number in below function
timeZone = timezone.time_zones_for_number(phoneNumber)
  
# It print the timezone of a phonenumber
print(timeZone)



# Program to find carrier and region of a phone number

# Parsing String to Phone number
phoneNumber = phonenumbers.parse("+40723450294")
  
# Getting carrier of a phone number
Carrier = carrier.name_for_number(phoneNumber, 'en')
  
# Getting region information
Region = geocoder.description_for_number(phoneNumber, 'en')
  
# Printing the carrier and region of a phone number
print(Carrier)
print(Region)
