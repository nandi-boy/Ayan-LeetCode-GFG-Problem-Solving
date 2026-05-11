class Solution(object):
    def isPalindrome(self, x):
        n=x
        sum = 0
        while x> 0:
            rem = x%10
            sum = sum*10 +rem
            x = x//10
        if n ==sum:
            return True
        else :
            return False


        