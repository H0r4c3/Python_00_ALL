'https://py-googletrans.readthedocs.io/en/latest/'

'''
Googletrans is a free and unlimited python library that implemented Google Translate API. 
This uses the Google Translate Ajax API to make calls to such methods as detect and translate.

Features
Fast and reliable - it uses the same servers that translate.google.com uses
Auto language detection
Bulk translations
Customizable service URL
Connection pooling (the advantage of using requests.Session)
HTTP/2 support
Note on library usage
The maximum character limit on a single text is 15k.
Due to limitations of the web version of google translate, this API does not guarantee that the library would work properly at all times. 
(so please use this library if you don’t care about stability.)
If you want to use a stable API, I highly recommend you to use Google’s official translate API.
If you get HTTP 5xx error or errors like #6, it’s probably because Google has banned your client IP address.

translate(text, dest='en', src='auto', **kwargs)
Translate text from source language to destination language

Parameters:	
text (UTF-8 str; unicode; string sequence (list, tuple, iterator, generator)) – The source text(s) to be translated. Batch translation is supported via sequence input.
dest – The language to translate the source text into. The value should be one of the language codes listed in googletrans.LANGUAGES or one of the language names listed in googletrans.LANGCODES.
dest – str; unicode
src – The language of the source text. The value should be one of the language codes listed in googletrans.LANGUAGES or one of the language names listed in googletrans.LANGCODES. If a language is not specified, the system will attempt to identify the source language automatically.
src – str; unicode
'''

from googletrans import Translator, LANGCODES

translator = Translator()

#print(LANGCODES)

#text = ['Textul acesta este in limba romana']
text = 'Textul acesta este in limba romana'
translations = translator.translate(text, dest='en', scr='ro').text
print(translations)

