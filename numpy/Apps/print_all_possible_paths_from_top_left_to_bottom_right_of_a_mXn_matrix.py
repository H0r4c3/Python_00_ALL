'https://www.geeksforgeeks.org/print-all-possible-paths-from-top-left-to-bottom-right-of-a-mxn-matrix/'

def printAllPathsUtil(mat, i, j, m, n, path, pi):
 
    # Reached the bottom of the matrix, so we are left with only option to move right
    if (i == m - 1):
        for k in range(j, n):
            path[pi + k - j] = mat[i][k]
 
        for l in range(pi + n - j):
            print(path[l], end = " ")
        print()
        return
 
    # Reached the right corner of the matrix, we are left with only the downward movement.
    if (j == n - 1):
 
        for k in range(i, m):
            path[pi + k - i] = mat[k][j]
 
        for l in range(pi + m - i):
            print(path[l], end = " ")
        print()
        return
 
    # Add the current cell to the path being generated
    path[pi] = mat[i][j]
 
    # Print all the paths that are possible after moving down
    printAllPathsUtil(mat, i + 1, j, m, n, path, pi + 1)
 
    # Print all the paths that are possible after moving right
    printAllPathsUtil(mat, i, j + 1, m, n, path, pi + 1)
 
    # Print all the paths that are possible after moving diagonal
    printAllPathsUtil(mat, i+1, j+1, m, n, path, pi + 1);
 
 
 
# The main function that prints all paths
# from top left to bottom right
# in a matrix 'mat' of size mXn
def printAllPaths(mat, m, n):
 
    path = [0 for i in range(m + n)]
    printAllPathsUtil(mat, 0, 0, m, n, path, 0)
 



mat = [[1, 2, 3],
       [4, 5, 6]]

# mat = [[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]]
 
printAllPaths(mat, 2, 3)