class Solution:
    def factorial(self,n):
        if n==1 or n==0:
            return 1
        else:
            return n*self.factorial(n-1)
            
    def isStrong(self, n):
        sum = 0
        org = n
        while n>0:
            digit = n%10
            sum = sum+self.factorial(digit)
            n = n//10
        return sum == org
        