
import time;
# Python program to count all possible paths
# from top left to bottom right

def numberOfPaths(m, n):
    # If either given row number is first
    # or given column number is first
    if (m == 1 or n == 1):
        return 1

    # If diagonal movements are allowed
    # then the last addition
    # is required.
    return numberOfPaths(m - 1, n) + numberOfPaths(m, n - 1)

def numOfPathFast(r, c):
    count = [[ 0 for x in range(c)] for y in range(r)]

    #print(count)

    for i in range(r):
        count[i][0]=1
    for j in range(c):
        count[0][j]=1
    #print(count)
    for ri in range (1, r):
        for cj in range (1, c):
            #print(str(ri)+", "+str(cj))
            count [ri][cj]= count [ri][cj-1] + count[ri-1][cj]
            #print(count)

    return count [r-1][c-1]




# Driver program to test above function
r = 3
c = 3

#print(numberOfPaths(r, c))
ticks1 = time.time()

print (numOfPathFast(r,c))