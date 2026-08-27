class Solution:
    def gfSeries(self, n):
        if n == 1:
            return [0]
        ans = [0, 1]
        for i in range(2, n):
            next_term = ans[i - 2] ** 2 - ans[i - 1]
            ans.append(next_term)
        return ans
        