'https://blog.devgenius.io/unleashing-power-of-recursion-to-solve-crossword-puzzles-d5b94737c916'

import logging

path_log = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\GUI\Crosswords\Crossword2\log_file.log'

#Create and configure logger
#logging.basicConfig(filename=path, format='%(asctime)s %(message)s', filemode='w', level=logging.DEBUG)

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG,
                    filename=path_log, 
                    filemode='w')

#logger = logging.getLogger('main')

crossword = ['.XXX.', 
             '...X.', 
             '.X.X.', 
             '.....']

'''
Result:
['AXXXT', 
 'BECXA', 
 'BXOXI', 
 'AICAR']
'''

my_path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\GUI\Crosswords\Crossword2\words.txt'

#words = "ICELAND;MEXICO;PANAMA;ALMATY"
#words = 'ABBA;BEC;COC;AICAR;TAIR'
#words = words.split(";")
#print(words)


def read_words_from_file(my_path):
        with open (my_path, 'r') as my_file_with_words:
            line = my_file_with_words.read().upper()
            words = line.split('\n')
        
        return words


def convert_to_matrix(crossword):
    logging.info('Start convert_to_matrix')
    for i in range(len(crossword)):
        crossword[i] = list(crossword[i])
    logging.debug(f'crossword = {crossword}')
    return crossword


def convert_to_string(crossword):
    for rows in range(len(crossword)):
        crossword[rows] = ''.join(crossword[rows])
    
    return crossword


def canPlaceHorizontally(crossword, word, rows, cols):
    logging.info(f'Start canPlaceHorizontally for rows = {rows} and cols = {cols}')
    M = len(crossword)
    N = len(crossword[0])
    
    if cols > 0 and crossword[rows][cols-1] != 'X':
        logging.debug(f'canPlaceHorizontally = False')
        return False
    elif (cols+len(word)-1) >= N or ((cols+len(word) < N) and (crossword[rows][cols+len(word)] != 'X')):
        logging.debug(f'canPlaceHorizontally = False')
        return False
    
    for i in range(len(word)):
        if(crossword[rows][(cols+i)] == '.' or crossword[rows][(cols+i)] == word[i]):
            continue
        else:
            logging.debug(f'canPlaceHorizontally = False')
            return False
        
    logging.debug(f'canPlaceHorizontally = TRUE TRUE TRUE')
    return True


def canPlaceVertically(crossword, word, rows, cols):
    logging.info(f'Start canPlaceVertically for rows = {rows} and cols = {cols}')
    M = len(crossword)
    N = len(crossword[0])
    if rows > 0 and crossword[rows-1][cols] != 'X':
        logging.debug(f'canPlaceVertically = False')
        return False
    elif (rows+len(word)-1) >= M or ((rows+len(word) < M) and (crossword[rows+len(word)][cols] != 'X')):
        logging.debug(f'canPlaceVertically = False')
        return False
    for i in range(len(word)):
        if(crossword[rows+i][cols] == '.' or crossword[rows+i][cols] == word[i]):
            continue
        else:
            logging.debug(f'canPlaceVertically = False')
            return False
        
    logging.debug(f'canPlaceVertically = TRUE TRUE TRUE')
    return True


def placeHorizontally(crossword, word, rows, cols):
    logging.info(f'Start placeHorizontally for rows = {rows} and cols = {cols}')
    wherePlaced = set()
    for i in range(len(word)):
        if crossword[rows][cols+i] == '.':
            crossword[rows][cols+i] = word[i]
            wherePlaced.add(cols+i)
            
    logging.debug(f'wherePlaced Horizontally = {wherePlaced}')
    logging.debug(f'crossword after placeHorizontally = {crossword}')        
    return wherePlaced


def placeVertically(crossword, word, rows, cols):
    logging.info(f'Start placeVertically for rows = {rows} and cols = {cols}')
    wherePlaced = set()
    for i in range(len(word)):
        if crossword[rows+i][cols] == '.':
            crossword[rows+i][cols] = word[i]
            wherePlaced.add(rows+i)
            
    logging.debug(f'wherePlaced Vertically = {wherePlaced}')
    logging.debug(f'crossword after placeVertically = {crossword}')
    return wherePlaced


def unplaceHorizontally(crossword, wherePlaced, word, rows, cols):
    logging.info(f'Start unplaceHorizontally for rows = {rows} and cols = {cols}')
    for i in range(len(word)):
        if cols+i not in wherePlaced:
            continue
        else:
            crossword[rows][cols+i] = '.'
            logging.debug(f'crossword after unplaceHorizontally = {crossword}')


def unplaceVertically(crossword, wherePlaced, word, rows, cols):
    logging.info(f'Start unplaceVertically for rows = {rows} and cols = {cols}')
    for i in range(len(word)):
        if rows+i not in wherePlaced:
            continue
        else:
            crossword[rows+i][cols] = '.'
            logging.debug(f'crossword after unplaceVertically = {crossword}')


def solution(crossword, words, idx):
    logging.info(f'Start solution for crossword = {crossword} and for idx = {idx}')
    if idx == len(words):
        crossword = convert_to_string(crossword)
        print(f'crossword_after_convert_to_string = {crossword}')
        logging.debug(f'crossword after convert_to_string = {crossword}')
        return True
    
    word = words[idx]
    print(f'word to check = {word}')
    logging.debug(f'word to check = {word}')
    
    for rows in range(len(crossword)):
        for cols in range(len(crossword[0])):
            if canPlaceHorizontally(crossword, word, rows, cols):
                wherePlaced = placeHorizontally(crossword, word, rows, cols)
                print(f'wherePlaced Horizontally = {wherePlaced}')
                
                if not solution(crossword, words, idx+1):
                    logging.debug(f'solution after canPlaceHorizontally = {solution(crossword, words, idx)}')
                    print(f'The word {word} does NOT match in wherePlaced Horizontally {wherePlaced}')
                    logging.info(f'The word {word} does NOT match in wherePlaced Horizontally {wherePlaced}')
                    unplaceHorizontally(crossword, wherePlaced, word, rows, cols)
                else:
                    print(crossword)
                    logging.debug(f'crossword (if solution after canPlaceHorizontally is True) = {crossword}')
                    return True
                
            if canPlaceVertically(crossword, word, rows, cols):
                wherePlaced = placeVertically(crossword, word, rows, cols)
                print(f'wherePlaced Vertically = {wherePlaced}')
                
                if not solution(crossword, words, idx+1):
                    logging.debug(f'solution after canPlaceVertically = {solution(crossword, words, idx)}')
                    print(f'The word {word} does NOT match in wherePlaced Vertically {wherePlaced}')
                    logging.info(f'The word {word} does NOT match in wherePlaced Vertically {wherePlaced}')
                    unplaceVertically(crossword, wherePlaced, word, rows, cols)
                else:
                    print(crossword)
                    logging.debug(f'crossword (if solution after canPlaceVertically is True) = {crossword}')
                    return True
                
    logging.debug(f'solution = False')
    return False

# START
crossword_matrix = convert_to_matrix(crossword)
print(f'crossword_matrix = {crossword_matrix}')

words = read_words_from_file(my_path)
#print(words)


words = ['ABBA', 'BEC', 'COC', 'AICAR', 'TAIR']

#words = ['ABBA', 'BEC', 'COC', 'AICAR', 'TAIR', 'GOVERNMENT', 'HEALTH', 'SYSTEM', 'COMPUTER', 'MEAT', 'YEAR', 'THANKS', 'MUSIC', 'PERSON', 'READING', 'METHOD', 'DATA', 'FOOD', 'UNDERSTANDING', 'THEORY']

result = solution(crossword_matrix, words, 0)
print(result)