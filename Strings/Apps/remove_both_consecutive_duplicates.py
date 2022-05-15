


def consecutive_position(st):
    ''' Find the letters that are repeated consecutive. These should be removed from the string'''
    ''' Add the position of the first letter in a list names "consec_position" '''
    consec_position = list()
    for i in range(len(st)-1):
        if st[i]==st[i+1]:
            consec_position.append(i)
            break
    return consec_position


def remove_consec_duplicates(st):
    global st_rem
    consec_position = consecutive_position(st)
    st_list = list(st)
    print('consec_pos = ', consec_position)
    if consec_position == []:
        st_rem = st
        print(st_rem)
        return st_rem
    else:
        del st_list[consec_position[0]]
        del st_list[consec_position[0]]
        st_rem = ''.join(st_list)
        print('st_rem = ', st_rem)
    
    remove_consec_duplicates(st_rem)
    

s = 'aabbHccdd'
s = 'asdcbsdcagfsdbgdfanfghbsfdab'
print("Result = ", remove_consec_duplicates(s))
print(st_rem)