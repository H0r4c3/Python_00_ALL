'https://www.geeksforgeeks.org/print-all-possible-paths-from-top-left-to-bottom-right-of-a-mxn-matrix/'

list_of_paths = list()

def printAllPathsUtil(mat, i, j, m, n, path, pi):
    global list_of_paths
    path_list = list()
 
    # Reached the bottom of the matrix, so we are left with only option to move right
    if (i == m - 1):
        for k in range(j, n):
            path[pi + k - j] = mat[i][k]
 
        for l in range(pi + n - j):
            path_list.append(path[l])
            print(path[l], end = " ")
        print()
        print(path_list)
        return path_list
 
    # Reached the right corner of the matrix, we are left with only the downward movement.
    if (j == n - 1):
 
        for k in range(i, m):
            path[pi + k - i] = mat[k][j]
 
        for l in range(pi + m - i):
            path_list.append(path[l])
            print(path[l], end = " ")
        print()
        print(path_list)
        return path_list
 
    # Add the current cell to the path being generated
    path[pi] = mat[i][j]
 
    # Print all the paths that are possible after moving down
    printAllPathsUtil(mat, i + 1, j, m, n, path, pi + 1)
 
    # Print all the paths that are possible after moving right
    printAllPathsUtil(mat, i, j + 1, m, n, path, pi + 1)
 
    # Print all the paths that are possible after moving diagonal
    printAllPathsUtil(mat, i+1, j+1, m, n, path, pi + 1)
 
 
 
# The main function that prints all paths
# from top left to bottom right
# in a matrix 'mat' of size mXn
def printAllPaths(mat, m, n):
 
    path = [0 for i in range(m + n)]
    list_of_all_paths = printAllPathsUtil(mat, 0, 0, m, n, path, 0)
    print(list_of_all_paths)
    
    return(list_of_all_paths)
 



# mat = [[1, 2, 3],
#        [4, 5, 6]]

# mat = [[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]]

mat =[[1, 6, 7, 2, 4],
      [0, 4, 9, 5, 3],
      [7, 2, 5, 1, 4],
      [3, 3, 2, 2, 9],
      [2, 6, 1, 4, 0]]
 
list_of_all_paths = printAllPaths(mat, 5, 5)
print(list_of_all_paths)




# # Original version of the code:
# # Python3 program to Print all possible paths from
# # top left to bottom right of a mXn matrix
 
# '''
# /* mat: Pointer to the starting of mXn matrix
# i, j: Current position of the robot
#      (For the first call use 0, 0)
# m, n: Dimensions of given the matrix
# pi: Next index to be filed in path array
# *path[0..pi-1]: The path traversed by robot till now
#                 (Array to hold the path need to have
#                  space for at least m+n elements) */
# '''
# def printAllPathsUtil(mat, i, j, m, n, path, pi):
 
#     # Reached the bottom of the matrix
#     # so we are left with only option to move right
#     if (i == m - 1):
#         for k in range(j, n):
#             path[pi + k - j] = mat[i][k]
 
#         for l in range(pi + n - j):
#             print(path[l], end = " ")
#         print()
#         return
 
#     # Reached the right corner of the matrix
#     # we are left with only the downward movement.
#     if (j == n - 1):
 
#         for k in range(i, m):
#             path[pi + k - i] = mat[k][j]
 
#         for l in range(pi + m - i):
#             print(path[l], end = " ")
#         print()
#         return
 
#     # Add the current cell
#     # to the path being generated
#     path[pi] = mat[i][j]
 
#     # Print all the paths
#     # that are possible after moving down
#     printAllPathsUtil(mat, i + 1, j, m, n, path, pi + 1)
 
#     # Print all the paths
#     # that are possible after moving right
#     printAllPathsUtil(mat, i, j + 1, m, n, path, pi + 1)
 
#     # Print all the paths
#     # that are possible after moving diagonal
#     # printAllPathsUtil(mat, i+1, j+1, m, n, path, pi + 1);
 
# # The main function that prints all paths
# # from top left to bottom right
# # in a matrix 'mat' of size mXn
# def printAllPaths(mat, m, n):
 
#     path = [0 for i in range(m + n)]
#     printAllPathsUtil(mat, 0, 0, m, n, path, 0)
 
# # Driver Code
# mat = [[1, 2, 3],
#        [4, 5, 6]]
 
# printAllPaths(mat, 2, 3)
 
# # This code is contributed by Mohit Kumar