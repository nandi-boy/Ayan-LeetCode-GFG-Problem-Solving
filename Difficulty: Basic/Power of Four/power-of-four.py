class Solution:
    def isPowerOfFour(self, n):
        while n%4 == 0:
            n = n//4
        return n == 1
        