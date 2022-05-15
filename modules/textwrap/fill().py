'https://www.geeksforgeeks.org/textwrap-text-wrapping-filling-python/'

'''
textwrap.fill(text, width=70, **kwargs): The fill() convenience function works similar to textwrap.wrap except it returns the data joined into a single, 
newline-separated string. This function wraps the input single paragraph in text, and returns a single string containing the wrapped paragraph.
'''


import textwrap
  
value = """This function returns the answer as STRING and not LIST."""
  
# Wrap this text
wrapper = textwrap.TextWrapper(width=50)
  
string = wrapper.fill(text=value)
  
print (string)