'https://betterprogramming.pub/stop-using-square-bracket-notation-to-get-a-dictionarys-value-in-python-c617f6ea15a3'

'''
Syntax:
dictionary.setdefault(keyname, value)

keyname	= Required. The keyname of the item you want to return the value from
value	= Optional. A value to return if the specified key does not exist. Default value = None

Sometimes, not only do you want to protect from an undefined term in your dictionary, but you also want your code to self-correct its data structures. 
The .setdefault() is structured identically to .get(). 
However, when the term is undefined, in addition to returning a default value, the dictionary’s term will be set to this value as well.

Where it differs from .get() is that the term and definition are now part of the dictionary

'''

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("price", 15000)
y = car.setdefault("price")
z = car.setdefault("brand")

print(x)
print(y)
print(z)

print(car.items())