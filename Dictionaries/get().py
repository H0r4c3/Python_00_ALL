'https://www.w3schools.com/python/ref_dictionary_get.asp'

'''
Syntax:
dictionary.get(keyname, value)

keyname	= Required. The keyname of the item you want to return the value from
value	= Optional. A value to return if the specified key does not exist. Default value = None
'''

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("price", 'The key "price" does not exist')
y = car.get("price")
z = car.get("brand")

print(x)
print(y)
print(z)

print(car.items())