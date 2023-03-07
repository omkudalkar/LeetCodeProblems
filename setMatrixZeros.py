'''
Author : Om K 
Description : Given a m x n matrix, if an element is 0, set entire row and column to 0. 
'''
def setMatrixZeros(matrix):
    # these two arrays keep track of the original location of zeros. 
    z_rows = []
    z_cols = []
    # this loop is simply to find the location of the zeros in our matrix. 
    i = 0
    while i < len(matrix):
        j = 0 
        while j < len(matrix[i]):
            if matrix[i][j] == 0:
                z_rows.append(i)
                z_cols.append(j)
            j+=1
        i+=1
    # after having found the location, we re-loop through the matrix and when we encounter 
    # the row or column which needs to made 0, we set all elements to zero. 
    i = 0
    while i < len(matrix):
        j = 0 
        while j < len(matrix[i]):
            if i in z_rows or j in z_cols:
                matrix[i][j] = 0
            j+=1
        i+=1
    return matrix 
     
# basic tests from Leetcode prompt
def tester():
    assert(setMatrixZeros([[1,1,1],[1,0,1],[1,1,1]])) == [[1,0,1],[0,0,0],[1,0,1]]
    assert(setMatrixZeros([[0,1,2,0],[3,4,5,2],[1,3,1,5]])) == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


tester()
     