class Solution:
    def isPrime(self, n):
        if n<=1:
            return False
        else:
            for i in range (2,n):
                if n%i == 0:
                    return False
                    break
            else:
                return True
            
        