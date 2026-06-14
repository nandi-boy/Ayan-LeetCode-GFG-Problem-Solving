class Solution:
    def getMinMax(self, arr):
        res=[]
        minimum = min(arr)
        res.append(minimum)
        maximum = max(arr)
        res.append(maximum)
        
        return res