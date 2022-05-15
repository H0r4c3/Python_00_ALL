'https://docs.python.org/3/library/textwrap.html'

'''
textwrap.shorten(text, width, *, fix_sentence_endings=False, break_long_words=True, break_on_hyphens=True, placeholder=' [...]')
Collapse and truncate the given text to fit in the given width.

First the whitespace in text is collapsed (all whitespace is replaced by single spaces). If the result fits in the width, it is returned. 
Otherwise, enough words are dropped from the end so that the remaining words plus the placeholder fit within width:
'''

import textwrap
  
a = textwrap.shorten("Hello  world!", width=12)
print(a)

b = textwrap.shorten("Hello  world!", width=11)
print(b)

c = textwrap.shorten("Hello world", width=10, placeholder="...")
print(c)

