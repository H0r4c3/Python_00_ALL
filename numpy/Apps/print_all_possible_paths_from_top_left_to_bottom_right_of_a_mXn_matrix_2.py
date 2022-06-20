'https://www.geeksforgeeks.org/print-all-possible-paths-from-top-left-to-bottom-right-of-a-mxn-matrix/'

# Python3 program to Print all possible paths from
# top left to bottom right of a mXn matrix
allPaths = []
def findPaths(maze,m,n):
    path = [0 for d in range(m+n-1)]
    findPathsUtil(maze, m, n, 0, 0, path, 0)
     
def findPathsUtil(maze,m,n,i,j,path,index):
    global allPaths
    # if we reach the bottom of maze, we can only move right
    if i == m-1:
        for k in range(j,n):
            #path.append(maze[i][k])
            path[index + k - j] = maze[i][k]
        # if we hit this block, it means one path is completed.
        # Add it to paths list and print
        print(path)
        allPaths.append(path)
        return
    
    # if we reach to the right most corner, we can only move down
    if j == n-1:
        for k in range(i,m):
            path[index + k - i] = maze[k][j]
          #path.append(maze[j][k])
        # if we hit this block, it means one path is completed.
        # Add it to paths list and print
        print(path)
        allPaths.append(path)
        return
     
    # add current element to the path list
    #path.append(maze[i][j])
    path[index] = maze[i][j]
     
    # move down in y direction and call findPathsUtil recursively
    findPathsUtil(maze, m, n, i+1, j, path, index+1)
     
    # move down in y direction and call findPathsUtil recursively
    findPathsUtil(maze, m, n, i, j+1, path, index+1)
    
 
if __name__ == '__main__':
    maze = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    findPaths(maze,3,3)
    #print(allPaths)