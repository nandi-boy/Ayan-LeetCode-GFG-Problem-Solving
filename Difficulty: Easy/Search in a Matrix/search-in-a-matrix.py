class Solution:
    def searchMatrix(self, mat, x): 
    	m = len(mat)
    	n = len(mat[0])
    	for i in range(m):
    	    for j in range(n):
    	        if mat[i][j] == x:
    	            return True
    	else:
    	   return False
    	
