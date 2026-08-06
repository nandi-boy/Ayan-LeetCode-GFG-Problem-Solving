class Solution:
    def missingNumber(self, arr):
        n = len(arr)+1
        add = 0
        for i in arr:
            add = add+i
            
        ex = n*(n+1)//2
        
        return ex-add
            
        
    
        