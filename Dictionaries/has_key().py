'https://www.educative.io/edpresso/how-to-check-if-a-key-exists-in-a-python-dictionary'


#1. 

Fruits = {'a': "Apple", 'b':"Banana", 'c':"Carrot"}
key_to_lookup = 'a'

if Fruits.has_key(key_to_lookup):
    print("Key exists")
else:
    print("Key does not exist")


# 2.

Fruits = {'a': "Apple", 'b':"Banana", 'c':"Carrot"}
key_to_lookup = 'a'
if key_to_lookup in Fruits:
    print("Key exists")
else:
    print("Key does not exist")
