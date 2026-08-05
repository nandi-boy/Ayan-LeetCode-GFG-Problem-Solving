class Solution:
    def sortedMerge(self, a, b):
        res = a+b
        res.sort()
        return res
        