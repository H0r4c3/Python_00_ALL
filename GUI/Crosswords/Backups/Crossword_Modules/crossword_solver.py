from collections import defaultdict

my_path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\GUI\Crosswords\Crossword_Modules\words.txt'

class CrosswordSolver:
    global my_path
    
    def __init__(self): 
        pass
    
    def read_words_from_file(self, my_path):
        with open (my_path, 'r') as words:
            line = words.read()
            list_of_words = line.split('\n')
        
        return list_of_words
    
    def convert_list_into_dict(self, list_of_words):
        dict_of_words = defaultdict(list)
        for item in list_of_words:
            dict_of_words[len(item)].append(item)
        
        return dict_of_words
    
    def all_words():
        
        all_h = [[(0,0)], [(0,4)], 
                 [(1,0), (1,1), (1,2)], [(1,4)],
                 [(2,0)], [(2,2)], [(2,4)],
                 [(3,0), (3,1), (3,2), (3,3), (3,4)]]
        
        all_v = [[(0,0), (1,0), (2,0), (3,0)],
                 [(1,1)], [(3,1)], 
                 [(1,2), (2,2), (3,2)], 
                 [(3,3)], 
                 [(0,4), (1,4), (2,4), (3,4)]]
        
    def words_positions(self, mask):
        # Parse the crossword
        n, m = len(mask), len(mask[0])
        mask = [list(row) for row in mask]
    
        # Find the word positions
        word_position = []
        for i in range(n):
            for j in range(m):
                if mask[i][j] == '.':
                    if j == 0 or mask[i][j-1] == 'X':
                        word_position.append((i, j, 'across'))
                    elif i == 0 or mask[i-1][j] == 'X':
                        word_position.append((i, j, 'down'))
        
        return word_position, mask
    
    def possible_words(self, word_pos, mask, list_of_words):
        '''
        Generate possib_words for each position
        '''
        possib_words = dict()
        n, m = len(mask), len(mask[0])
        mask = [list(row) for row in mask]
        
        for i, j, direction in word_pos:
            if direction == 'across':
                length = 1
                while j+length < m and mask[i][j+length] == '.':
                    length += 1
                pattern = ''.join(mask[i][j:j+length])
            else:
                length = 1
                while i+length < n and mask[i+length][j] == '.':
                    length += 1
                pattern = ''.join(mask[k][j] for k in range(i, i+length))
                
            possib_words[(i, j, direction)] = [word for word in list_of_words if len(word) == length and all(word[k] == pattern[k] or 
                                                                                                           pattern[k] == '.' for k in range(length))]
            
        #print(possib_words)
        return possib_words
    
    def backtrack(self, mask, pos, word_position, possib_words):
        '''
        Fill in the crossword
        '''
        if pos == len(word_position):
            return True, mask
        i, j, direction = word_position[pos]
        for word in possib_words[(i, j, direction)]:
            if all(word[k] == mask[i][j+k] or mask[i][j+k] == '.' for k in range(len(word))):
                # Fill in the word
                for k in range(len(word)):
                    mask[i][j+k] = word[k]
                # Recursively backtrack
                if self.backtrack(mask, pos+1, word_position, possib_words):
                    return True, mask
                # Undo the fill
                for k in range(len(word)):
                    mask[i][j+k] = '.'
        return False, mask
    

def main():
    print('For starting the program, you must use App.py!')    
    
if __name__ == "__main__":
    main()
    
    
    