'https://python.plainenglish.io/ultimate-python-cheat-sheet-f2930e08669c'

Python Cheat Sheet
Naming conventions

# Variable lower_snake
firstName = 'MuhammadUmair'

# Class and module CamelCase
class UserDetails:

# Constant All Capital/UpperCase
USER_AGE = 100 # All uppercase

# Indentation : 4 spaces
if USER_AGE > 18:
    print('You can go to the party.')
    
Data type
name = 'MuhammadUmair' # string
age = 21 # int
height_in_foot = 5.833 # float
is_married = False # boolean
cousins = ['Usama', 'Jawad', 'Anas'] # list
address = ('Shahdara', 'Lahore', 'Pakistan') # tuple
possessions = { 'Phone': 'Infinix Note 7 Lite', 'Laptop': "Lenovo IdeaPad 510" } # dict

Type conversion
# Python is a strong type language
age = 20 + "1" # TypeError

# Convert to string
age = 20 + int("1") # 21

# Convert to string
my_age = str(5.833) # "5.833"

# Convert to number
my_height = int(5.833) # 5
my_number = float('5.833') # 5.833

# Get type
type(my_age) # <class 'str'>
type(my_number) # <class 'float'>

# Check if number 0 to 9
isdigit('8') # True

# Check type
isinstance(my_number, int) # True
Strings
name = 'Umair'
# or
name = "Umair"
# or
about = """I am Muhammad
Umair AKram Software Enginerr likes to 
Work in Python,MERN(MongoDB,Express,React,Node),Selenium."""

# escape characters \n will do a line break
message = "Muhammad \nUmair"

# raw string (ignore escape characters)
information = r"https://amianumair.medium.com/data-science-the-path-to-unlocking-the-best-paying-job-roles-in-the-near-future-932a21b9df89#418f-99174a22f344"

# Convert to lower case
name.lower() # umair

# Convert to upper case
name.upper() # UMAIR

# Convert first char to Capital letter
name.capitalize() # Umair

# Convert first char of all words to Capital letter
name = 'muhammad umair'
name.title() # Muhammad Umair

# Chain methods
name = 'uMair'
name.lower().capitalize() # Umair

name = 'Umair'

# Start with ?
name.startswith('U') # true

# End with ?
name.endswith('r') # true

# String length
len(name) # 5

# String concatenation
full_name = first_name + ' ' + last_name

# String format
full_name = f"{first_name} {last_name}"

# Remove leading and trailing characters (like space or \n)
text = 'I am Muhammad Umair Akram  Software Engineer '
text.strip() # 'i am muhammad umair akram software engineer'

name = 'Umair'
# Get string first character
name[0] # U

# Get string last character
name[-1] # r

# Get partial string
name[1:3] # ma

# Replace
name.replace('U', 'O') # Omair

# Find (return pos or -1 if not found)
name.find('r') # 4

# List to string
cousins = ['Usama', 'Jawad', 'Anas']
', '.join(cousins) # 'Usama, Jawad, Anas'
Commons functions
# Print to console
print('Muhammad Umair')

# Print multiple string
print('Muhammad', 'Umair') # Muhammad Umair

# Multiple print
print(10 * '*') # **********

# Variable pretty printer (for debug)
from pprint import pprint
pprint(cousins) # will output var with formatting

# Get keyboard input
name = input('What is your name? ')

# Random (between 0 and 1)
from random import random 
print(random()) # 0.26230234411558273

# Random beween x and y
from random import randint
print(randint(5, 11)) # 6

# Rounding
number = 5.8
print(round(number)) # 6

number = 5.8333
print(round(number, 2)) # 5.83

# Path
import os
current_file_path = __file__
folder_name = os.path.dirname(current_file_path)
new_path = os.path.join(folder_name, 'new folder')

# Round number
solution = round(5.8333, 2) # 5.83
Conditionals
if age == 18:
    print('age is 18')
elif age != 18 and age < 20:
   print('age is not 18 and is less than 20')
else:
   print('age is 21 or greater than 20')

#In or not in
cousins = ['Usama', 'Jawad', 'Anas']
if 'Anas' in cousins:
if 'Ahmad' not in cousins:

# Ternary
print('age = 10') if age == 10 else print('age != 10') 

# ShortHand Ternary
is_aged = 'Aged'
msg = is_aged or "Not Aged" # 'Aged'

# Falsy
False, None, 0, empty string "", empty list [], (), {}

# Truthy
True, not zero and not empty value
Iterations
# iterating over a sequence (list, string, etc.)
items=[1,2,3,4,5]
for item in items:
    print(item)

# With index
for index, item in enumerate(items):
    print(index, item)

# Range
for number in range(10):  #0..9
    print(number)

for number in range(5, 10): #5..9
    print(number)

# While loop
while number > 10:
    print(number)
    # exit loop
    if number == 5:
        break
    # Jump to next while
    if number == 3:
        continue

    number += 1

# For loop dic 
possessions = { 'Phone': 'Infinix Note 7 Lite', 'Laptop': "Lenovo IdeaPad 510" }
for key, value in possessions.items():
    print(key, value)

# List comprehension: 
# values = [(expression) for (value) in (collection)]
items = [value*2 for value in items]

# List comprehension filtering
# values = [expression for value in collection if condition]
even_squares = [x * x for x in range(10) if x % 2 == 0]
List and Tuple
# Create a list
customers = ['Ali', 'Fatima', 'Muneeb']

# Append to List
customers.append('Hashim')

# List length
nb_items = len(customers)

# Remove from list
del customers[1]   #remove apple

# List access
customers[0]  # first item
customers[-1] # last item

# Slice my_list[start:finish:step] ([::-1] reverse list) 
customers = customers[1:3]
customers[:3]  # first 3
customers[2:]  # last 2
copy_customers = customers[:] # copy

# List length
nb_entry = len(customers) 

#Create list from string
colors = 'ali, fatima, muneeb'.split(', ')

# Array concact
names1 = ['umair', 'ahmad']
names2 = ['ali', 'haider']
names3 = names1 + names2

# Concat by unpacking
names3 = [*names1, *names2]

# Multiple assignment
name, version= ['Lenovo', 510]

#Create a Tuple (kind of read only list)
address = ('shahdara', 'lahore', 'pakistan')

# Sort
names.sort() # ['Ali', 'Fatima', 'Muneeb']
names.sort(reverse=True) # ['Muneeb', 'Fatima', 'Ali']
names.sort(key=lambda name: len(name)) # ['Ali', 'Fatima', 'Muneeb']
Dictionaries
# Create a empty dict
products = {}

#Create a dict with key/value
products = {'name': "Lenovo", 'phone': 'Infinix'}

# Access dict value by key
print(products['name']) # Lenovo

# Access dict
products.get('name') # if key not exist return None
products.get('name', 'Name of Product') # if key not exist return Name of Product

# Adding a new key/value
products['version'] = "510"

# Get dict keys
product.keys() # ['name', 'phone', 'version']

# Get dic values
products.values() # ['Lenovo', 'Infinix', '510']

# Create a list of dict
products = [
    {'rollNo': 005, 'name': 'MuhammadUmair'},
    {'rollNo': 102, 'name': 'Hashim'},
    {'rollNo': 179, 'name': 'Ibrar'},
]

# Access list of dict
print(products[2]['name']) # Hashim

# Search list dict
items_match = [item for product in products if product['id'] == 179]
# [{'id': 179, 'name': 'Ibrar'}]

# Sum list dict
total = sum([product['price'] for product in products])
Functions
# Create a function
def greetings():
    print('Hello Reader, all my love and respect is for you an only you')

# Function with argument (with default value)
def greetings(name = 'reader'):
    print(f"Hello {name}") 

# Function with argument (with optional value)
def greetings(name = None):
    if name:
        print(f"Hello {name}") 
    else:
        print('Hello Reader')

# Call a function
greetings('Neil') # Hello Mike

# Call using keyword argument
greetings(name = 'Ali') 

# Function returning a value
def Addition(number1, number2):
   return number1 + number2

num = Addition(10, 20) # 30

# Arbitrary numbers of arguments *args
def greetings(*names):
    for name in names:
        print(f"Hello {name}")

# Arbitrary numbers of keywords arguments **kwargs
def greetings(**kwargs):
    print(kwargs['name'])
    print(kwargs['age'])

greetings(name = 'Umair', age = 45)

# Lambda function
AddTen = lambda num : num + 10
print(AddTen(20)) # 30
Date and time
from datetime import datetime, timedelta

# Return the current date and time.
datetime.now()

# Create a date time object
date = datetime(2000,04,09) # April 09 2000

# Add to date/time (weeks, days, hours, minutes, seconds) 
new_year = date + timedelta(days=1) # April 10 2000

# Format a date to string
new_year.strftime('%Y/%m/%d %H %M %S') # 2021/01/01 00 00 00 
new_year.strftime('%A, %b %d') # Friday, Jan 01

# Extract from date
year = new_year.year # 2021
month = new_year.month # 01
File
# Reading a file and storing its lines
filename = 'bio.txt'
with open(filename) as file:
    lines = file.readlines()

for line in lines:
    print(line)

# Writing to a file
filename = 'bio.txt'
with open(filename, 'w') as file:
    file.write("Love lives even after the Death")

# File exist?
from os import path
path.exists('templates/index.html') # True/False

# CSV
import csv
csv_file = 'export.csv'
csv_columns = products[0].keys() # ['id', 'name']
with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for item in products:
        writer.writerow(item)
Catching an exception
age_string = input('Your age? ')
try:
    age = int(age_string)
except ValueError:
    print("Please enter a numeric value")
else:
    print("Your age is saved!")
OOP
# Create a class
class Items:
    pass

# Class attribute
class Item:
    nb_items = 0

print(Product.nb_items) # 0

# Create new object instance
item_1 = Item()

# Object instance attributes
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Create instance with attributes
item_1 = Item('Lenovo IdeaPad 510', 60,000)
item_2 = Item('Infinix Note 7 Lite', 25,000)
print(item_1.name) # Lenovo IdeaPad 510

# instance method
class Item()
    def display_price(self):
        return f"Price : {self.price}"

print(item_1.display_price())

# class method
class Item:
    # ... 
    @classmethod
    def create_default(cls):
        # create a instance 
        return cls('Item', 0) # default name, default price

item_3 = Item.create_default() 

# static method
class Item:
    # ... 
    @staticmethod
    def trunc_text(word, nb_char):
        return word[:nb_char] + '...' 

item_3 = Item.trunc_text('This is a blog', 5) # This i... 

# Python Inheritance
class WebProduct(Product):
    def __init__(self, name, price, web_code):
        super().__init__(name, price)
        self.web_code = web_code

# Private scope (naming convention only)
def __init__(self, price):
    self.__price = price

# Getter and setter
class Item:
    def __init__(self):
        self.__price = 0

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

# Mixins
class Mixin1(object):
    def test(self):
        print "Mixin1"

class Mixin2(object):
    def test(self):
        print "Mixin2"

class MyClass(Mixin2, Mixin1, BaseClass):
    pass

obj = MyClass()
obj.test() # Mixin2