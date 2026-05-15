class Solution:
    def printNos(self, n):
        if n==0:
            return 0 
        self.printNos(n-1)
        print(n,end=' ')
        
        
            
            