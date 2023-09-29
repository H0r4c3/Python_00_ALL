# Best Solution: 
# https://py.checkio.org/mission/crossword-solver/publications/Rcp8jzd/python-3/backtracking-filling-the-most-constrained-words-first/?ordering=most_voted&filtering=all

from typing import List, Tuple
import re

my_path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\GUI\Crosswords\Crossword_OK\words.txt'

class CrosswordSolver:
    """ A class for solving a crosswords grid """

    def __init__(self, crossword, words):
        self.grid = [list(row) for row in crossword]
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.dictionary = words
        self.used_words = set()
    
    def read_words_from_file(self, my_path):
        with open (my_path, 'r') as words:
            line = words.read().upper()
            list_of_words = line.split('\n')
        
        return list_of_words

    def find_empty(self) -> None or Tuple[str, tuple, tuple]:
        """
        Find an empty or partially filled word in the given crossword. If
        several words are partially filled, choose the one which has more
        constrained letters.
        :return: empty or partially filled word, start and end of the word
        """
        empties = set()
        for i, row in enumerate(self.grid):
            if '.' in row:
                j = row.index('.')
                for dx in (-1, 1):
                    # Is the word vertical?
                    if 0 <= i + dx < self.height and self.grid[i + dx][j] != \
                            'X':
                        line = ''.join(self.grid[k][j] for k in range(
                            self.height))
                        start = (line.rfind('X', 0, i) + 1, j)
                        end = (self.height if line.find('X', i) == -1
                               else line.find('X', i), j + 1)
                        empties.add((line[start[0]:end[0]], start, end))
                for dy in (-1, 1):
                    # Is the word horizontal?
                    if 0 <= j + dy < self.width and self.grid[i][j + dy] != \
                            'X':
                        line = ''.join(row)
                        start = (i, line.rfind('X', 0, j) + 1)
                        end = (i + 1, self.width if line.find('X', j) == -1
                               else line.find('X', j))
                        empties.add((line[start[1]:end[1]], start, end))
        if not empties:
            return None
        return max(empties, key=lambda empty: len(empty[0]) - empty[
            0].count('.'))

    def find_possible(self, pattern: str) -> List[str]:
        """
        Find all words that match the given pattern
        find_possible('s...c.') -> ['search', 'source', 'speech', 'switch']
        :param pattern: A partially filled word, where '.' represents unknown
                        letters
        :return: All words in the dictionary that fully match the given pattern
        """
        return [re.fullmatch(pattern, word).group(0)
                for word in self.dictionary if re.fullmatch(pattern, word)
                and word not in self.used_words]

    def insert_word(self, word, start, end):
        """ Insert a word in the grid at the given coordinates """
        k = 0
        for i in range(start[0], end[0]):
            for j in range(start[1], end[1]):
                self.grid[i][j] = word[k]
                k += 1

    def solve(self) -> bool:
        """ Main program recursively called until the grid is finished """
        find = self.find_empty()

        # We finished the crossword!
        if find is None:
            return True

        pattern, start, end = find
        possible_words = self.find_possible(pattern)
        # Pick a word out of the possible words
        for word in possible_words:
            # Insert the word in the grid
            self.insert_word(word, start, end)
            self.used_words.add(word)

            # And see if we can find a solution with this supposition
            if self.solve():
                return True

            # Undo the word insertion if we can't find a solution
            self.insert_word(pattern, start, end)
            self.used_words.remove(word)
        return False

    def tolist(self):
        """ Format the solution so that it is understood by the checker """
        return [''.join(row) for row in self.grid]
    
    
    def solver_(crossword, words):
        cs = CrosswordSolver(crossword, words)
        cs.solve()
        return cs.tolist()