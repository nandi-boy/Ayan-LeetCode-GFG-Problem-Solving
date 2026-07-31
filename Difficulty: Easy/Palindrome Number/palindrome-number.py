class Solution:
    def isPalindrome(self, n):
        org = n
        n=abs(n)
    	rev = 0
    	while n>0:
    	    d = n%10
    		rev = rev*10+d
    		n = n//10
        
    	if org <0:
    	    rev=-rev
		if rev == org:
		    return True
    	else:
    		 return False
		
		