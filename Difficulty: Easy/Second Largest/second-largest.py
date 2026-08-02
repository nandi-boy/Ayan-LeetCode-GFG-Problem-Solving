class Solution:
    def getSecondLargest(self, arr):
        arr.sort()
        largest = arr[-1]
        for i in range(len(arr)-2,-1,-1):
            if arr[i] != largest:
                return arr[i]
                break
        else:
            return -1
            
        