'''
Transform a string from '000123+000456' into '123+456'
'''

import re
 
def strip_zeros_from_digits(log):
    log_split = re.split(r'(\D)', log) # split after non-numeric chars
    print(log_split)
    
    log_split_strip = [item.lstrip('0') for item in log_split]
    print(log_split_strip)
    
    new_log = ''.join(log_split_strip)
    
    return new_log


log = '000123+000456'
log = '000123+000456+000444-000888'
log = '-5-10+15-'

new_log = strip_zeros_from_digits(log)
print(new_log)