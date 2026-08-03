class Solution:
    def transpose(self, mat):
        m = len(mat)
        n = len(mat[0])
        res = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                res[i][j] = mat[j][i]
                
        return res
        