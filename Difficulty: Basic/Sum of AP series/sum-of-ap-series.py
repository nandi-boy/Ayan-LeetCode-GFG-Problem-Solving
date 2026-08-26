class Solution:
    def sumOfAP(self, n, a, d):
        sum_val = 0
        for i in range(n):
            sum_val = sum_val+a
            a = a+d
        return sum_val
            
        