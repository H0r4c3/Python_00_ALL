'https://www.geeksforgeeks.org/remove-elements-to-make-array-sorted/'

# 1. Method: 
'''
Approach: Traverse the given array and for every element which is greater than or equal to the previously taken element, add this element to another array else skip to the next element. In the end, the newly created array will be sorted according to Stalin sort. 

For each element check if the element is greater than the previous element or not. 
If yes then check for the next element.
Else remove that element.
After all the elements have been traversed, we will get a sorted array.
'''

# Function to sort the array
# by removing misplaced elements
def removeElements_(arr,  n) :
 
    # brr[] is used to store
    # the sorted array elements
    brr = [0]*n 
    l = 1
 
    brr[0] = arr[0]
    for i in range(1, n) :
        if (brr[l - 1] <= arr[i]):
            brr[l] = arr[i]
            l += 1
 
    # for i in range(l) :
    #     print(brr[i], end=" ")

    return brr[ : l]
 
 
# 2. Method: Instead of using an extra array, store them in the same array  

def removeElements(list):
            
    # j stores the index
    j = 1
    for i in range(1, len(list)):
        if list[j - 1] <= list[i]:
            list[j] = list[i]
            j += 1
        
    return list[ : j]
  
 

if __name__ == "__main__" :
 
    my_list = [10, 12, 9, 10, 2, 13, 14]
    n = len(my_list)
    
    result = removeElements(my_list)
    print(result)