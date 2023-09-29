'https://medium.com/@vanacorec/backtracking-and-crossword-puzzles-4abe195166f9'

'''
Backtracking and Crossword Puzzles
In this blog, I wanted to explore the concept of backtracking and look at a couple of applications of it. Then, I decided to see if backtracking could be applied to crossword puzzles. I was able to use backtracking to create a crossword puzzle answer key that worked reasonably well on very small grids, but not as well on larger grids.

Recursion
Backtracking algorithms rely on recursion, so to understand backtracking, you have to understand recursion. In general,

recursion is a method of solving a problem by defining the problem in terms of smaller problems of the same kind.

In programming, this translates to calling a function within itself. Though recursion is not necessarily computationally faster, the code is often simpler.

Recursion Examples

https://www.xkcd.com/1739/
The python code for this would be:

def what_are_you_working_on():
    print("tried to fix the problems I created when I ")
    what_are_you_working_on()
print("Trying to fix the problems I created when I")
what_are_you_working_on()


As you can see, this loop goes on forever. To prevent infinite loops, recursive algorithms need to include a base condition, also called a termination condition, to stop the recursion at a point where the problem can be solved without further recursion. There is no obvious base case for this scenario, so let’s look at a different example.

Factorial by Recursion
By definition, the factorial of n is equal to the product of n and all smaller positive integers. In order to use recursion to solve this, we need to break the problem down into “smaller problems of the same type.” We can do this by thinking of the factorial of n as n times the factorial of n-1. Then the factorial of n-1 is n-1 times the factorial of n-1-1… and so on until you hit the base case: factorial of 1 = 1.

5! = 5 * 4 * 3 * 2 * 1 = 120
5! = 5 * 4!
where 4! = 4 * 3!
where 3! = 3 * 2!
where 2! = 2 * 1!
where 1! = 1
Here is the python code for this:

def factorial(n):
    if n == 1:  #base case
        return 1
    else:   #recursive case
        return n * factorial(n-1)
    
factorial(5)
In this case, the base case is “if n == 1: return 1,” because we don’t need any more recursion to solve that problem. The function will continue to call itself until this base case is reached.

Call Stack
Recursive functions work because of the “call stack,” which is a data structure that stores information about the active subroutines of a computer program. Each time a program calls a function, the function is added to the top of the call stack. When something is returned, the top function is removed from the top of the call stack, and the value is returned to the next function.

After adding in print statements to our code above, we can see how the call stack is working.

def factorial(n):
    print("factorial call with n = ", n)
    if n == 1: #base case
        print("base case: result for factorial( 1 ): 1")
        return 1
    else: #recursive case
        temp = n * factorial(n-1)
        print("result for", n,"* factorial(",n-1,"): ",temp)
        return temp
factorial(5)

Here’s a visualization of how the call stack is working:




Backtracking
Now that we understand recursion, we can get back to backtracking. From Wikipedia:

Backtracking is a general algorithm for finding all (or some) solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate (“backtracks”) as soon as it determines that the candidate cannot possibly be completed to a valid solution.

Backtracking works well for problems in which the solution has well-defined constraints and the solution can be built incrementally, with “partial candidate solutions.” To understand how this works, let’s look at backtracking applied to sudoku.

The rules of sudoku are that a number cannot appear more than once in any column, row, or box. Here is a solved sudoku board:


As you can see, each number appears only once in each column, row, and box. These rules serve as our constraints for the problem.

If we wanted to the solve a sudoku puzzle, one way to do that would be to generate every configuration of numbers 1 through 9 in the empty cells, checking each full board to see if the constraints are met. If there are n blank squares in the puzzle, there would be 9^n full boards to check. If 50 of the 81 squares start off blank, then there are 5.1537752 * 10^47 different combinations of boards.

Using backtracking, we check the solutions along the way to prevent ourselves from creating a lot of solutions that are not viable.

We do this by working by filling in one empty cell at a time, create “partial candidate solutions.” Every time we go to put a number in a cell, we check the constraints: Is the number not already in the column? Is the number not already in the row? Is the number not already in the box?

If we can assign a number there with no conflict, we do it and recursively move to the next cell. If we can’t assign a number there, we backtrack to the previous cell and update that number.

The pseudocode for this is:

Find row, col of an unassigned cell
If there is none, return true
For digits from 1 to 9
   a) If there is no conflict for digit at row, col
assign digit to row, col and recursively try fill in rest of grid
   b) If recursion successful, return true
   c) Else, remove digit and try another
If all digits have been tried and nothing worked, return false
Here’s a good video that visualizes what is going on in a 4 by 4 matrix.


https://www.youtube.com/watch?v=_vWRZiDUGHU
The base case is that there are no more empty cells to look at, which stops the recursive function and returns the full solution.

8 Queens Puzzle
Another problem that can be solved using backtracking is the 8 queens puzzle. The goal of the puzzle is to place 8 queens on a chess board so that none of them attack each other, meaning no queens can share a row, column, or diagonal.


Instead of looking at all the possible ways that 8 queens can be places on the board, and then evaluating each possible configuration to see if it meets the constraints of no queens attacking each other, we can use backtracking methods to eliminate configurations along the way.

The thought process behind a backtracking algorithm to solve this puzzle is: Start with the next empty square. If there is no queen in the row, column or diagonal, place a queen, then recursively call the function again to move to the next empty square. If no queen can be placed, then backtrack to the previous queen and try the next square. In this scenario, the base case is that there is enough queens have been placed, which indicates that the puzzle has been solved. Recursion and the call stack are what allow us to move backwards to the previous queen placement.

This is how the algorithm works on the smaller scale of a 4x4 grid:


This recursive process continues until it hits the base case, where all the queens have been placed, and gives the solution:


Depth-First Search with Pruning
The partial candidates represented as the nodes of a tree structure, the potential search tree. Each partial candidate is the parent of the candidates that differ from it by a single extension step. In the case of the queens problem, each extension step is another queen placed.

The backtracking algorithm traverses this search tree recursively, from the root down, in depth first order.


Depth First Search Tree Pruning for the N-Queens Puzzle

Can backtracking be applied to crossword puzzles?
After exploring how backtracking can be applied to Sudoku and the 8 Queens Puzzle, I wanted to see if it could be applied to crossword puzzles in some manner. Conceptually, solving a crossword puzzle could be done with using backtracking, but the “constraints” would be complicated to deal with because the clues are ambiguous and different for each word on the board.

So instead of solving a crossword puzzle using the clues, I wanted to see if I could use backtracking to create a crossword puzzle, basically making the answer key and not worrying about the clues yet.



http://rexwordpuzzle.blogspot.com/2012/02/co-anchor-hill-of-early-show-wed-2-8-12.html
For crossword puzzles, the constraint is that every horizontal and vertical sequences of boxes up to a shaded square must be a valid word, from left to right or top to bottom respectively.

I created “partial candidate solutions” by moving letter by letter through the puzzle, starting with the top left corner and continuing along each row until I got the end of the row. For each letter that is placed, in order to satisfy the constraints, the horizontal and vertical strings of boxes needed to be part of a valid word. In order to check if this, I imported a dictionary of all english words and used regular expressions to see if there were words in the dictionary that matched the patterns.

Simple Pseudocode for my create board function:

def create():
  find the next empty square in the board
  for each letter in the alphabet
    if the letter can create valid words
      place it in the square
      create()
I had my function print out when it was “backtracking,” which is when there were no valid letters to put in a square so it moved back to the previous square and tried the next letter.

Here is output starting with a 3 x 3 empty grid:


Here is part of an attempt with a 5x5 board.


Updates:

I was able to cut down on computation time by trimming the word list at the beginning of the function. I created a new word list that only contained words up to the length of the longest possible word in the puzzle. This sped up the process a lot by reducing how many words the check letter function needed to search through each time.
At first, in a grid of the same length and height, words repeated themselves. I implemented an additional check when inputting a letter that would complete a word, to see if the word is already in the grid.
Looping through the letters alphabetically was not ideal. I added a weighting system that would order the letter by checking to see which letters would have the most possible words and then placing that letter in the square. This made each step take longer, but decreased the overall time that the algorithm took because it had to backtrack fewer times, and got to the solution more quickly.
Future Improvements:

Expanding the dictionary to include more than just the English dictionary- acronyms, proper nouns, multiple word answers, etc.
Adding functionality to place certain words in the puzzle and not have them changed by the backtracking methods
Take aways:

Although the code was relatively simple, it wasn’t that efficient. I want to test if creating all the possible grids and then checking which ones were valid at the end could be faster.
A Few More Examples
4 x 3 blank board:


5 x 4 blank board:


5 x 4 blank board with reversed alphabet:


5 x 4 blank board with shuffled alphabet: ‘fgonbljdhmkurwiacxptesyqvz’


5 x 5 blank board with shaded squares:


Sources
https://en.wikipedia.org/wiki/Recursion_(computer_science)

https://en.wikipedia.org/wiki/Backtracking

http://toolsandtoys.net/the-new-york-times-mini-crosswords-volume-1/

https://brilliant.org/wiki/recursive-backtracking/

https://www.youtube.com/watch?v=_vWRZiDUGHU

https://www.geeksforgeeks.org/sudoku-backtracking-7/

https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/tutorial/

https://en.wikipedia.org/wiki/Call_stack

https://realpython.com/python-thinking-recursively/

https://www.xkcd.com/1739/

'''