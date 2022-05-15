'https://coderzcolumn.com/tutorials/python/difflib-simple-way-to-find-out-differences-between-sequences-file-contents-using-python'

'''
Python provides us with a module named difflib which can compare sequences of any type for us so that we don't need to write 
complicated algorithms to find common subsequences between two sequences. 
The difflib module provides different classes and methods to perform a comparison of two sequences and generate a delta.

At the core of the difflib module is SequenceMatcher class which implements an algorithm responsible for comparing two sequences. 
It requires that all the elements of both sequences be hashable in order for them to work. 
It first finds the longest common subsequence between two sequences and then divides both sequences into left parts of both original 
sequences (left subsequences of original sequences) and right parts of both original sequences (right subsequences of original sequences) 
based on that common subsequence. It then recursively perform the same function of finding the longest common subsequence on the left parts of 
both original sequences and the right parts of both original sequences.

Important Methods of SequenceMatcher Instance
find_longest_match(alo=0, ahi=None, blo=0, bhi=None) - This method accepts the starting and ending indices of both sequences and returns longest 
common matching subsequence between two sequences as Match instance.
The Match instance is a named tuple and has three attributes namely a, b, and size. 
The a and b attributes specify indices in first and second sequences from where the common sequence starts. The size specifies the length of the subsequence.
get_matching_blocks() - It returns a list of Match instances which has information about the list of matching subsequences between two sequences.
'''

import difflib

l1 = [1,2,3,5,6,7,8,9]
l2 = [2,3,6,7,8,10,11]

seq_mat = difflib.SequenceMatcher(a=l1, b=l2)

#match = seq_mat.find_longest_match(alo=0, ahi=len(l1), blo=0, bhi=len(l2))
match = seq_mat.find_longest_match()

print("============ Longest Matching Sequence ==================")
print("\nMatch Object : {}".format(match))
print("Matching Sequence from l1 : {}".format(l1[match.a:match.a+match.size]))
print("Matching Sequence from l2 : {}\n".format(l2[match.b:match.b+match.size]))