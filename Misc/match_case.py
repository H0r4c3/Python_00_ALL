'https://www.pythonpool.com/match-case-python/'

'''
The match case consists of three main entities :

The match keyword
One or more case clauses
Expression for each case
The case clause consists of a pattern to be matched to the variable, a condition to be evaluated if the pattern matches, 
and a set of statements to be executed if the pattern matches.

We can write multiple case statements for multiple possibilities for a given variable. Each case statement has a pattern that has to be matched.

The syntax looks something like this:

match variable_name:
            case ‘pattern1’ : //statement1
            case ‘pattern2’ : //statement2
            …            
            case ‘pattern n’ : //statement n
'''

quit_flag = False
match quit_flag:
    case True:
        print("Quitting")
        exit()
    case False:
        print("System is on") 