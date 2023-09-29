'https://blog.devgenius.io/unleashing-power-of-recursion-to-solve-crossword-puzzles-d5b94737c916'

crossword = [
    '++++++-+++',
    '++------++',
    '++++++-+++',
    '++++++-+++',
    '+++------+',
    '++++++-+-+',
    '++++++-+-+',
    '++++++++-+',
    '++++++++-+',
    '++++++++-+',

]

words = "ICELAND;MEXICO;PANAMA;ALMATY"
words = words.split(";")


def convert_2_matrix():
    for i in range(len(crossword)):
        crossword[i] = list(crossword[i])


def convert_to_string():
    for rows in range(len(crossword)):
        crossword[rows] = ''.join(crossword[rows])


convert_2_matrix()


def canPlaceHorizontally(arr, word, rows, cols):
    M = len(arr)
    N = len(arr[0])
    if cols > 0 and arr[rows][cols-1] != '+':
        return False
    elif (cols+len(word)-1) >= N or ((cols+len(word) < N) and (arr[rows][cols+len(word)] != '+')):
        return False
    for i in range(len(word)):
        if(arr[rows][(cols+i)] == '-' or arr[rows][(cols+i)] == word[i]):
            continue
        else:
            return False

    return True


def canPlaceVertically(arr, word, rows, cols):
    M = len(arr)
    N = len(arr[0])
    if rows > 0 and arr[rows-1][cols] != '+':
        return False
    elif (rows+len(word)-1) >= M or ((rows+len(word) < M) and (arr[rows+len(word)][cols] != '+')):
        return False
    for i in range(len(word)):
        if(arr[rows+i][cols] == '-' or arr[rows+i][cols] == word[i]):
            continue
        else:
            return False

    return True


def placeHorizontally(arr, word, rows, cols):
    wherePlaced = set()
    for i in range(len(word)):
        if arr[rows][cols+i] == '-':
            arr[rows][cols+i] = word[i]
            wherePlaced.add(cols+i)
    return wherePlaced


def placeVertically(arr, word, rows, cols):
    wherePlaced = set()
    for i in range(len(word)):
        if arr[rows+i][cols] == '-':
            arr[rows+i][cols] = word[i]
            wherePlaced.add(rows+i)
    return wherePlaced


def unplaceHorizontally(arr, wherePlaced, word, rows, cols):
    for i in range(len(word)):
        if cols+i not in wherePlaced:
            continue
        else:
            arr[rows][cols+i] = '-'


def unplaceVertically(arr, wherePlaced, word, rows, cols):
    for i in range(len(word)):
        if rows+i not in wherePlaced:
            continue
        else:
            arr[rows+i][cols] = '-'


def solution(arr, words, idx):

    if idx == len(words):
        convert_to_string()
        print(crossword)
        return True
    word = words[idx]
    for rows in range(len(crossword)):
        for cols in range(len(crossword[0])):
            if canPlaceHorizontally(arr, word, rows, cols):
                wherePlaced = placeHorizontally(arr, word, rows, cols)
                if not solution(arr, words, idx+1):
                    unplaceHorizontally(arr, wherePlaced, word, rows, cols)
                else:
                    return True
            if canPlaceVertically(arr, word, rows, cols):
                wherePlaced = placeVertically(arr, word, rows, cols)
                if not solution(arr, words, idx+1):
                    unplaceVertically(arr, wherePlaced, word, rows, cols)
                else:
                    return True

    return False


result = solution(crossword, words, 0)
print(result)