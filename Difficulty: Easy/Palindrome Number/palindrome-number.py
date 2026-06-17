class Solution:
    def isPalindrome(self, n):
        x = n
        rev = 0
        n = abs(n)
        while n>0:
            d = n%10
            rev = rev*10+d
            n = n//10
        if x<0:
            rev = -rev
        
        if x==rev:
            return True
        