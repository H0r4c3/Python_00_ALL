'https://blog.finxter.com/python-dictionary-how-to-create-add-replace-retrieve-remove/?tl_inbound=1&tl_target_all=1&tl_form_type=1&tl_period_type=3'

'''
To replace a key in an existing key:value pair, use the pop() method. This method updates an existing dictionary key with a new key.

'''

composers = {'Chopin':  1810,
             'Greeg':   1843,
             'Handel': 1684,
             'Mozart': 1756
            }
composers['NEW_Greeg'] = composers.pop('Greeg')
print(composers)