class Solution:
    def getMinMax(self, arr):
        mini = arr[0]
        maxi = arr[0]
        for i in range(len(arr)):
            if arr[i]<mini:
                mini = arr[i]
            elif arr[i] > maxi:
                maxi = arr[i]
        minmax = [mini,maxi]
            
        return minmax