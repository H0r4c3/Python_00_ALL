import re


pattern = '.'
pattern = re.sub('\.', '\.', pattern)
print(f'pattern1 = {pattern}')

pattern = '*'
pattern2 = re.sub('\*', '.+', pattern)
print(f'pattern2 = {pattern2}')

pattern = '?'
pattern3 = re.sub('\?', '.', pattern)
print(f'pattern3 = {pattern3}')

pattern = '[!0]'
pattern4 = re.sub('\!', '^', pattern)
print(f'pattern4 = {pattern4}')

pattern = '[!abc]name.txt'
pattern5 = re.sub('\[\!', '[^', pattern)
print(f'pattern5 = {pattern5}')

pattern = '[]'
pattern6 = re.sub('\[\]', '\[\]', pattern)
print(f'pattern6 = {pattern6}')

pattern = '[!]check.txt'
pattern7 = re.sub('\[\!\]', '\[\!\]', pattern)
print(f'pattern7 = {pattern7}')

pattern = '[c[]heckio'
pattern8 = re.sub('\[c\[\]', 'c', pattern)
print(f'pattern8 = {pattern8}')
