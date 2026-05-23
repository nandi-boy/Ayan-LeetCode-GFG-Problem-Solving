import math

class Solution:
    def gcd(self, n, arr):
        ans = arr[0]
        for i in range(1, n):
            ans = math.gcd(ans, arr[i])
        return ans
        
        