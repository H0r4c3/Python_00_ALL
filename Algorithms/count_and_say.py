'https://algo.quora.com/?__ni__=0&__tiids__=43369463&__filter__=all&__nsrc__=notif_page&__sncid__=20717816876&__snid3__=28584918960#anchor'

'https://algomart.quora.com/Interview-Problem-Count-and-Say'

'https://algomart.quora.com/'

'''
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"

countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. 
Then for each group, say the number of characters, then say the character. 
To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

Example:
Input: n = 4 
Output: "1211" 

Explanation:

countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
'''

def count_and_say(n):
    if n == 1:
        return 1
    
    n = str(n)
    
    if len(n) == 1:
        return '1' + n
    
    counter = 1
    result = ''
    
    for i in range(len(n)-1):
        print(f'i = {i}')
        if n[i] == n[i+1]:
            counter += 1
            
            if i == len(n) - 2:
                result = result + str(counter) + n[i]
                print(f'result_ = {result}')
                return result
                
        else:
            if i == len(n) - 2:
                result = result + str(counter) + n[i] + str(counter) + n[i+1]
                return result
            
            result = result + str(counter) + n[i]
            counter = 1
            print(f'result = {result}')
            
    return result


if __name__ == '__main__':
    
    n = 4 # -> 1211
    #n = 3322251 # -> 23321511
    n = 233553333656652
    n = 33

    result = count_and_say(n)
    print(result)