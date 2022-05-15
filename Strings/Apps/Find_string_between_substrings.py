
def find_string_between_chars(full_string):
    start_string = '<font color="green">'
    end_string = '</font>'
    start = full_string.rfind(start_string) + len(start_string)
    print(full_string.find(start_string))
    end = full_string.find(end_string)
    result = full_string[start:end]
    
    return result

full_string = '<font color="green">16</font>'
print("My String is:", find_string_between_chars(full_string))
