class Solution:
    def nthPosition (self, n):
            ans = 1
            while ans * 2 <= n:
                ans = ans * 2
            return ans
            