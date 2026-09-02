class Solution:
    def countOfElements(self, x, arr):
        c = 0
        for i in arr:
            if i <= x:
                c = c+1
        return c

