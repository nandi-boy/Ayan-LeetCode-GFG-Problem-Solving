class Solution:
    def kthDigit(self, a, b, k):
        dp = a**b
        d = str(dp)
        return int(d[-k])
        