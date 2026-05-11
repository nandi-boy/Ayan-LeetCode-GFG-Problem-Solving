class Solution:
    def getSecondLargest(self, arr):
        ma_x = -1
        second_max = -1
        
        for i in range (len(arr)):
            if arr[i]>ma_x:
                ma_x = arr[i]
                
        for i in range (len(arr)):    
            if arr[i]>second_max and arr[i]!= ma_x:
                second_max = arr[i]
                
        return second_max
        
            