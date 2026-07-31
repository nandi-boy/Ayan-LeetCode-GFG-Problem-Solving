class Solution:
    def findElements(self,arr):
        arr.sort()
        ar=[]
        for i in range (len(arr)-2):
            ar.append(arr[i])
        return ar
    
