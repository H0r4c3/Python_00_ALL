'https://regexone.com/'

'https://regexone.com/references/python'

'https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial'

'https://docs.python.org/3/library/re.html'

'https://realpython.com/regex-python/'

'https://realpython.com/lessons/plain-class-matching/'

'https://pythex.org/'

'https://blog.finxter.com/python-regex-match/'

'https://regex101.com/#python'

'https://www.regular-expressions.info/examples.html'

'https://regexr.com/'
'''


match()
Determine if the RE matches at the beginning of the string.
re.match("c", "abcdef")    # No match

search()
Scan through a string, looking for any location where this RE matches.
This method stops after the first match!
Synthax:
matchObject = re.search(pattern, input_str, flags=0)
Example:
re.search("c", "abcdef")   # Match

findall()
Find all substrings where the RE matches, and returns them as a list.
print(re.findall("c", "abcdecf")) # ['c', 'c']

finditer()
Find all substrings where the RE matches, and returns them as an iterator.

Hint:
When writing regular expression in Python, it is recommended that you use raw strings instead of regular Python strings. 
Raw strings begin with a special prefix (r) and signal Python not to interpret backslashes and special metacharacters in the string, 
allowing you to pass them through directly to the regular expression engine.

This means that a pattern like "\n\w" will not be interpreted and can be written as r"\n\w" instead of "\\n\\w" as in other languages, 
which is much easier to read.

Example: 
re.search(r'\bno\b', 'nobody knows nothing - no?')        # search for the word 'no' (only 'no', not included in another word!!!)
Without the raw string, Python would assume that it’s an unescaped backslash character '\', followed by the character 'b'.
With the raw string, all backslashes will just be that: backslashes. 
The regex engine then interprets the two characters as one special metacharacter: the word boundary '\b'

FLAGS:
In the Python regular expression methods above, you will notice that each of them also take an optional flags argument. 
Most of the available flags are a convenience and can be written into the into the regular expression itself directly, but some can be useful in certain cases.

re.IGNORECASE makes the pattern case insensitive so that it matches strings of different capitalizations
re.MULTILINE is necessary if your input string has newline characters (\n), this flag allows the start and end metacharacter (^ and $ respectively) to 
match at the beginning and end of each line instead of at the beginning and end of the whole input string
re.DOTALL allows the dot (.) metacharacter match all characters, including the newline character (\n)
'''

import re



'https://regexone.com/lesson/introduction_abcs'

print(re.match("c", "cabcdef"))
print(re.search("c", "abcdecf"))
print(re.findall("c", "abcdecf"))


s = 'foo123bar5'
# [0-9] matches any single decimal digit character—any character between '0' and '9', inclusive. 
# [0-9] matches any single decimal digit character—any character between '0' and '9', inclusive. 
print(re.search('[0-9][0-9][0-9]', s))

# the character \d can be used in place of any digit from 0 to 9
print(re.search('\d\d\d', s))

# the character \D can be used in place of any Non-digit character
print(re.search('\D\D\D', s))

# the . (dot) metacharacter can match any single character (letter, digit, whitespace, everything)
print(re.search('ba.', s))

# \. is matching the . (dot) character
s1 = 'fo.o123bar5'
print(re.search('\.', s1))

# the pattern [abc] will only match a single a, b, or c letter and nothing else
s2 = 'afoo123barc5'
print(re.findall('[abc]', s2))
print(re.match('[abc]', s2))

# the pattern [^abc] will match any single character except for the letters a, b, or c
s2 = 'afoo123barc5'
print(re.findall('[^abc]', s2))

# [a-z] = characters from a to z
# [0-9] = numbers from 0 to 9
s2 = 'afoo123barc5'
print(re.findall('[a-z]', s2))
print(re.findall('[0-9]', s2))

# \w = Any Alphanumeric character (equivalent to the character range [A-Za-z0-9_])
s3 = 'afo#o1$23b$ar&c5'
print(re.findall('\w', s3))

# \W = Any Non-alphanumeric character
s3 = 'afo#o1$23b$ar&c5'
print(re.findall('\W', s3))

# a{3} will match the 'a' character exactly three times.
# a{1,3} will match the 'a' character no more than 3 times, but no less than 1 time
# [wxy]{5} = five characters, each of which can be w, x, or y
# .{2,6} = between two and six of any character
s4 = 'aabcdeaaaluhd4aa332faklk'
print(re.findall('a{2,3}', s4))


# * = zero or more repetitions
# + = 1 or more repetitions
# \d* to match any number of digits
# \d+ which ensures that the input string has at least one digit
# a+ = one or more a's
# [abc]+ = one or more of any a, b, or c character
s4 = 'aa1bcd22eaaa33luhd4aa332faklk'
print(re.findall('\d*', s4))
print(re.findall('\d+', s4))
print(re.findall('[abc]+', s4))

string = """Hello my Number is 123456789 and my friend's number is 987654321"""
regex1 = '\d+'             
match1 = re.findall(regex1, string) 
print(match1)

regex2 = '\d'             
match2 = re.findall(regex2, string) 
print(match2)


# '?' = optionality
# ab?c will match either the strings "abc" or "ac", because the b is considered optional
s5 = 'aa1abcd22eaaac33luhd4abac332bfaklk'
print(re.findall('ab?c', s5))


# \s = a whitespace (The most common forms of whitespace you will use with regular expressions are the space (␣), the tab (\t), 
# the new line (\n) and the carriage return (\r) (useful in Windows environments))
# \S = any non-whitespace character
s5 = 'aa1 abcd2\r2eaaac\n33luhd4abac\t332bfaklk'
print(re.findall('\s', s5))
print(re.findall('\S', s5))


# ^ (hat) = starts
# $ (dollar sign) = ends
# ^success to match only a line that begins with the word "success"
# Note that this is different than the hat used inside a set of bracket [^...] for excluding characters
s6 = 'abcd342abcdef333def'
print(re.findall('^abc', s6))
print(re.search('def$', s6))


# (abc) = Any subpattern inside a pair of parentheses will be captured as a group. 
# ^(file.+)\.pdf$ = lines that start with "file" and have the file extension ".pdf"; for example: file_record_transcript.pdf
s6 = 'abcd342abcdef333defab'
print(re.search('^(abc)', s6))


# nested group (sub-group) (abc(de))
# ^(IMG(\d+))\.png$ = using a nested parenthesis to capture the digits
s6 = 'abcde342abcdf333defab'
print(re.findall('(abc(de))', s6)) # find 'abcde' and find 'de'


# abc(d3)? = optional group
s6 = 'abcd342abcdef333defab'
print(re.findall('(abc)(d3)?', s6))


# (abc)|(def) = abc OR def
# ([cb]ats*|[dh]ogs?) would match either cats or bats, or, dogs or hogs
# I love (cats|dogs) would match 'I love cats' OR 'I love dogs'
s6 = 'abcd342abcdef333defab'
print(re.findall('(abc)|(d3)', s6))



'https://regexone.com/references/python'

# Lets use a regular expression to match a few date strings.
regex = r"[a-zA-Z]+ \d+"
matches = re.findall(regex, "June 24, August 9, Dec 12")
for match in matches:
    # This will print:
    #   June 24
    #   August 9
    #   Dec 12
    print("Full match: %s" % (match))
    
    
# To capture the specific months of each date we can use the following pattern
regex = r"([a-zA-Z]+) \d+"
matches = re.findall(regex, "June 24, August 9, Dec 12")
for match in matches:
    # This will now print:
    #   June
    #   August
    #   Dec
    print("Match month: %s" % (match))


# If we need the exact positions of each match
regex = r"([a-zA-Z]+) \d+"
matches = re.finditer(regex, "June 24, August 9, Dec 12")
for match in matches:
    # This will now print:
    #   0 7
    #   9 17
    #   19 25
    # which corresponds with the start and end of each match in the input string
    print("Match at index: %s, %s" % (match.start(), match.end()))
    
    






'https://www.udemy.com/course/python-complete-course-for-beginners-h/learn/lecture/24345916#overview'

# search for 'ape' in a string
if re.search('ape', 'The tape was there'):
    print('ape found!')
    
# findall() returns a list of matches
# . is used to match any 1 character or space
my_string = 'The ape was at the apex'
allApes = re.findall('ape.', my_string)
print(allApes)
    

# finditer() returns an iterator of matching objects
# you can use 'span()' to get the location
for item in re.finditer("ape", my_string):
    location = item.span()
    print(location)

# square brackets will match any of the characters between the brackets
animalStr = 'Cat rat mat fat pat'
allAnimals = re.findall('[crmfp]at', animalStr)
print(allAnimals)

# characters in a range
allAnimals = re.findall('[c-mC-M]at', animalStr)
print(allAnimals)

# use ^ to exclude some characters
allAnimals = re.findall('[^Cr]at', animalStr)
print(allAnimals)


# you can compile a regex into pattern objects which provides additional methods
owlFood = 'rat cat mat pat'
regex = re.compile('[cr]at')
# sub() replaces items that match the regex in the string with the first parameter passed to sub
owlFood = regex.sub('owl', owlFood)
print(owlFood)


# backslash + special character
randStr = 'F.B.I.'
periods = re.findall('.\.', randStr) # the first period = any char; the backslash + the second period = period
print(periods)


# replacing new line chars (\n) with spaces
randStr = ''' This is a
long string that
goes on many lines
'''
# remove newlines \n
regex = re.compile('\n')
randStr = regex.sub(' ', randStr)
print(randStr)


# matching any single number
# \d can be used instead of [0-9]
# \D is the same as [^0-9]
randStr = '1a2b3c4d5'
print(re.findall('\d', randStr))
print(re.findall('\D', randStr))


# matching multiple digits using \d{number of digits}
print(re.findall('\d{5}', '0 123456'))

# match values that are between 5 and 7 digits
numStr = '123 1234 12345 123456 1234567'
print(re.findall('\d{5,7}', numStr))


# matching any single letter or number
# \w is the same as [a-zA-Z0-9_]
# \W is the same as [^a-zA-Z0-9_]
phNum = '123-456-7890'
# check if it is a phone number
print(re.search('\w{3}-\w{3}-\w{4}', phNum))
# check for valid first name between 2 and 20 characters
print(re.search('\w{2,20}', '#$% Ultraman'))


# matching white space
# \s is the same as [\f\n\r\t\v]
# \S is the same as [^\f\n\r\t\v]

# check for valid first and last name with a space
print(re.search('\w{2,20}\s\w{2,20}', 'FirstName LastName'))


# matching 1 or more characters
# match 'a' folowed by 1 or more characters
print(re.findall('a+', 'a as ape bug'))



'https://levelup.gitconnected.com/regular-expressions-22bbd24ac439'

# Match either Apple or apple
r = '[aA]pple'

# Match the letter ‘x’ or ‘y’ or ‘z’
r = '[xyz]'

# A single-digit will be matched 
# Dash (-) with [] is used to specify any one character in a range
r = '[0-9]'

# () Operator - It constructs a grouping construct to establish a precedence order and parenthesis is also 
# useful for OR’ing two expressions with the bar | character.
r = '(fact|smart)'

# Match any digit character [0–9]
r = '\d'

# Match any non-digit character
r = '\D'

# Match white spaces
r = '\s'

# Match non-white spaces
r = '\S'

# Match only brackets
r = '[(){}[\]]'

# Match word characters
# Matches any word character (alphanumeric & underscore). Only matches low-ascii characters (no accented or non-roman characters). 
# Equivalent to [A-Za-z0-9_]
r = '\w'

# Match non-word characters
r = '\W'

# If the ^ caret symbol is the first symbol after opening the square brace, it specifies the negation operation.
# ^ specifies that not an upper case letter
r = '[^A-Z]'

# ^ and $ can be called as most common anchors in regular expressions. ^ matches the start of a line and $ matches the end of the line.
# ^ Specifies the start of the sentence
r = '^Apple'

# $ Specifies the end of the sentence
r = 'manufacturer$'

# Both ^ and $ have been used to specify the whole sentence “Apple is the world’s 4th-largest PC vendor.”
r = '^Apple is the world’s 4th-largest PC vendor.$'

# The OR operator allows us to specify different allowable capture groups
# Match both “4th-largest” and “fourth-largest”
r = '(4th|fourth)-largest'

# The ? operator matches 0 or 1 of the preceding token, effectively making it optional.
# u is optional (match both color and colour)
r = 'colou?r'

# The * operator matches 0 or more of the preceding token.
# It should have zero or more occurrences of the character “o” (match oh and ooh and oooooh)
r = 'oo*h'

# The + operator matches 1 or more of the preceding token.
# It should have zero or more occurrences of the “o” (match oh and ooh and h)
r = 'o+h'

# The dot . operator matches any character except linebreaks.
# Between “r” and “n” it can have different letters but only one letter (match ran and run and ron)
r = 'r.n'

# Numerical range is used to specify a quantity range using {low, high}
# Minimum should have 4 digits and maximum should have 6 letters 
# {n,} — minimum is n and maximum is undefined
r = '\w{4,6}'

# \b matches the word boundary and \B is used to identify non-word boundary
# Matches with “the” either “The” or “the” but do not match the word “other”
r = '\b[Tt]he\b'

# Matches with “the” as a non-word boundary and not match for word “the” (match 'other', but not 'the')
r = '\B[t]he\B'


# Matches any email address(???)
my_string = 'abc@gmail.com def@gmail.com'
regex = '\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b'

email_addresses = re.findall(regex, my_string)
print(email_addresses)


# Matches texts inside the quotation marks: " "
my_string = '"Lorem Ipsum" is simply dummy text '
pattern = r'"([^"]*)"'
result = re.findall(pattern, my_string)
print(result)


# Matches any single character (\w) and then its repetitions (\1*), if any:
my_string = 'sdsffffse'
pattern = re.compile(r'(.)\1*')
result_iterator = pattern.finditer(my_string)
result = [match.group() for match in result_iterator]
print(f'result = {result}')


# Matches every word after a 'keyword=' -> 'light'
my_string = 'theme=light; sessionToken=abc123'
keyword = 'theme'
pattern = re.compile(keyword + '=([\w]+)')
pattern = re.compile('theme=([\w]+)')
result = pattern.search(my_string).group(1)
print(result)


# Matches a word with repetition of letters
my_string = 'aaabbbcdddeeefggg'
pattern = re.compile('a+b+c+d+e+f+g+')
result = pattern.search(my_string)
print(result)


# Matches the word Python followed by ! or by ?
my_string = 'Abc def Python? Python! Python Python? DEF'
pattern = re.compile('Python(!|\?)')
result = pattern.search(my_string)
print(result)


# Matches "ruby" or "ruble"
my_string = 'Abc def ruby ruble DEF'
pattern = re.compile('rub(y|le)')
result = pattern.search(my_string)
print(result)


# Match "Python" or "Python, python, python", etc.
my_string = 'Abc def Python, python, python DEF'
pattern = re.compile('([Pp]ython(, )?)+')
result = pattern.search(my_string)
print(result)


# Matches words starting with capital letter
my_string = 'Abc def Python, python, python DEF'
pattern = re.compile('[A-Z][a-z]*')
result = pattern.findall(my_string)
print(result)


# Checking the strength of a password: 
# The password will be considered strong enough if:  
# - containing one lowercase letter
# - containing one uppercase letter
# - it has at least one digit
# - its length is greater than or equal to 10 symbols
password = 'bAse730onE4'
regex = '(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{10,})' # (?= is named 'Positive lookahead' (instead of AND !!!!)
print(re.findall(regex, password))
'''
EXPLANATIONS for (?=(.*).*\1)
. - any symbol except '\n'
* - 0 or more repetitions of the previous symbol
.* - several symbols
(.*) - brackets are a capturing group. It is used to catch and “memorize” what we matched inside the brackets (a repeating substring we are looking for)
next .* means that there might be any number (including 0) of symbols between the repetitions
\1 means the same string we found in the first capturing group (our substring).
(?=pattern) - is a positive lookahead. It matches if pattern matches next, but doesn’t consume any of the string. 
In terms of our task it helps us to find all the repeating substrings. 
If we typed just '(.*).*\1' (without the lookaround), we would find only the first repeating substring, 
because it would consume some parts of the string and wouldn’t be able to find the other repeating substrings.
'''


# Select the text that appears within parentheses
text = "Put vacation photos online (They were so cute) a few yrs ago. PC crashed, and now I forget the name of the site (I'm crying)."

# Write a greedy regex expression to match
regex = r"\(.+?\)"
sentences_found_greedy = re.findall(regex, text)
print(text)
print(sentences_found_greedy)





# Capturing Groups
# Repeat a capturing group (\d)+ vs Capture a repeated group (\d+)
my_string = 'My lucky numbers are 8755 and 33'

repeat_a_capturing_group = re.findall(r'(\d)+', my_string)

capture_a_repeated_group = re.findall(r'(\d+)', my_string)

print(f'repeat_a_capturing_group = {repeat_a_capturing_group}')
print(f'capture_a_repeated_group = {capture_a_repeated_group}')

'''
Explanations for Capturing Groups:

In the first code, we use findall to match a capturing group containing one number. 
We want this capturing group to be repeated once or more times. 
We get 5 and 3 as an output because these numbers are repeated consecutively once or more times.
 
In the second code, we specify that we should capture a group containing one or more repetitions of a number.
'''


# Groups: Extract only the names 
my_string = 'Claire has 2 friends who she spends a lot of time with. Susan has 3 brothers, while John has 4 sisters.'
# Use parantheses to group and capture characters together
only_names = re.findall(r'([A-Za-z]+)\s\w+\s\d+\s\w+', my_string)
print(f'only_names = {only_names}')


# Groups: Extract the names + the number + friends/brothers/sisters
# We add the parentheses to group together each of the three parts of the regex. In the output, we got a list of tuples. 
# The first element of each tuple is the match captured corresponding to group one. The second to group two. The last to group three.
# We can use capturing groups to match a specific subpattern in a pattern. We can use this information for retrieving the groups by numbers
three_groups = re.findall(r'([A-Za-z]+)\s\w+\s(\d+)\s(\w+)', my_string)
print(f'three_groups = {three_groups}')


# Groups: Select a group by number
three_groups = re.search(r'([A-Za-z]+)\s\w+\s(\d+)\s(\w+)', my_string)
print(f'three_groups_1 = {three_groups.group(1)}') # group nr. 1
print(f'three_groups_2 = {three_groups.group(2)}') # group nr. 2
print(f'three_groups_3 = {three_groups.group(3)}') # group nr. 3
print(f'three_groups_0 = {three_groups.group(0)}') # all 3 groups


# Groups: Using numbered captured groups to reference back
sentence = 'I wish you a happy happy birthday'

'''We want to find all matches of repeated words. In the code, we specify that we want to capture a sequence of word characters. Then a whitespace.
Then we write backslash one. This will indicate that we want to match the first group captured again. 
In other words, it says match that sequence of characters that was previously captured once more. 
And we get the word happy as an output. This was the repeated word in our string.
'''
repeated_word = re.findall(r'(\w+)\s\1', sentence)
print(f'repeated_word = {repeated_word}')

'''
Now, we will replace the repeated word with one occurrence of the same word. 
In the code, we use the same regex as before. This time, we use the dot sub method. 
In the replacement part, we can also reference back to the captured group. We write r backslash one inside quotes. 
This says replace the entire expression match with the first captured group. 
In the output string, we have only one occurrence of the word happy.
'''

replaced = re.sub(r'(\w+)\s\1', r'\1', sentence)
print(f'replaced = {replaced}')



# Look-ahead
'''
This non-capturing group checks whether the first part of the expression is followed or not by the lookahead expression. 
As a consequence, it will return the first part of the expression. In the previous example, we are looking for the word cat. 
The look ahead expression can be either positive or negative. For positive, we use question mark equal(?=). 
For negative question mark exclamation mark (?!).
'''
my_text = 'abc.txt lookahead_expression, def.txt lookahead_expression, ghi.txt non_lookahead_expression'
first_part = re.findall(r'\w+\.txt(?=\slookahead_expression)', my_text)
print(f'first_part = {first_part}') # returns only the first part of the expression, if the first part is followed by lookahead_expression


# Look-behind
'''
Get all the matches that are preceded or not by a specific pattern
For positive, we use (?<=lookbehind_expression)
'''


# using GROUP to select a text between 2 tags
my_text = '''<h>123abc</h>
             <li>456def</li>'''

text_h = re.findall(r'<h>.*</h>', my_text)
print(text_h)

# now, modify the middle, using group (paranthesis)
text_between_h = re.findall(r'<h>(.*)</h>', my_text)
print(text_between_h)


# Extract chars between numbers
'''
Here's the breakdown of the regex:
(?<=\d): Positive lookbehind to assert that the pattern is preceded by a digit (\d).
[^\d]+: One or more non-digit characters, which is the actual pattern you want to match.
(?=\d): Positive lookahead to assert that the pattern is followed by a digit (\d).
'''
my_text = '-=-+135-++--+-257=-'
#result = re.findall(r'[\d]+(.*)[\d]+', my_text) -> works only for digits!!!
pattern = r'(?<=\d)[^\d]+(?=\d)'
result = re.findall(pattern, my_text)
print(result)


# Extract numbers with signs
my_text = '-=-+135-++--+-257=-'
result = re.findall(r'[+-]{1}[\d]+', my_text)
result = re.findall(r'[+-]?[\d]+', my_text)
print(f'result = {result}')



