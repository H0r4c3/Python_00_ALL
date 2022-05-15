'https://www.geeksforgeeks.org/sha-in-python/'

'''
SHA, ( Secure Hash Algorithms ) are set of cryptographic hash functions defined by the language to be used 
for various applications such as password security etc. Some variants of it are supported by Python in the “hashlib” library. 
These can be found using “algorithms_guaranteed” function of hashlib.

Functions associated :
encode() : Converts the string into bytes to be acceptable by hash function.
hexdigest() : Returns the encoded data in hexadecimal format.
'''

import hashlib
  
# prints all available algorithms
print ("The available algorithms are : ", end ="")
print (hashlib.algorithms_guaranteed)



import hashlib
  
# initializing string
str = "GeeksforGeeks"
  
# encoding GeeksforGeeks using encode()
# then sending to SHA256()
result = hashlib.sha256(str.encode())
  
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA256 is : ")
print(result.hexdigest())
  
print ("\r")
  
# initializing string
str = "GeeksforGeeks"
  
# encoding GeeksforGeeks using encode()
# then sending to SHA384()
result = hashlib.sha384(str.encode())
  
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA384 is : ")
print(result.hexdigest())
  
print ("\r")
  
# initializing string
str = "GeeksforGeeks"
  
# encoding GeeksforGeeks using encode()
# then sending to SHA224()
result = hashlib.sha224(str.encode())
  
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA224 is : ")
print(result.hexdigest())
  
print ("\r")
  
# initializing string
str = "GeeksforGeeks"
  
# encoding GeeksforGeeks using encode()
# then sending to SHA512()
result = hashlib.sha512(str.encode())
  
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA512 is : ")
print(result.hexdigest())
  
print ("\r")
  
# initializing string
str = "GeeksforGeeks"
  
# encoding GeeksforGeeks using encode()
# then sending to SHA1()
result = hashlib.sha1(str.encode())
  
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())




def checkio(hashed_string, algorithm):
    return  hashlib.new(algorithm, hashed_string.encode()).hexdigest()

print(checkio('happy spam', 'sha224'))