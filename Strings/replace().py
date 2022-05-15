'https://www.datacamp.com/community/tutorials/python-string-replace?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=278443377095&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=1011845&gclid=EAIaIQobChMIpZvC-sfB8gIVb0aRBR0ePA3nEAAYASAAEgIsMvD_BwE'

'''
string.replace(old, new, <count>)
old − This is the old substring to be replaced.
new − This is the new substring, which would replace the old substring.
count − If this optional argument count is given, only the first count occurrences are replaced.

Python provides you with the .replace() string method that returns a copy of the string with all the occurrences 
of old substring replaced with the new substring given as a parameter.
'''

my_string = 'The red house is between the blue house and the old house.'
print(my_string)

my_string2 = my_string.replace('house', 'car')
print(my_string2)

path1 = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\modules\PIL\DSCN1369.JPG'
path2 = path1.replace('.JPG', '_2.JPG')
print(path1)
print(path2)