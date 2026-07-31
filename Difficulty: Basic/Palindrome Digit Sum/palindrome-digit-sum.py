class Solution:
    def isDigitSumPalindrome(self, n):
        org = n
        c = 0
    	while n>0:
    	    d = n%10
    		c=c+d
    		n = n//10
        org_sum = c
        rev = 0
        while c>0:
    	    dt = c%10
    		rev=rev*10+dt
    		c = c//10
    	if org_sum == rev:
    	    return True
    	else: 
    	    return False
        