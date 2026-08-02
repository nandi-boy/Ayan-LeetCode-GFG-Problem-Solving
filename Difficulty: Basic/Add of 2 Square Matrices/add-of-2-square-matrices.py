class Solution:
    def addMat(self, a, b):
        m = len(a)
        n = len(a[0])

        for i in range(m):
            for j in range(n):
                a[i][j] = a[i][j]+b[i][j]

        return a