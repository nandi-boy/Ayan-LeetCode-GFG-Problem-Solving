class Solution:
    def isPower(self, x, y):
        if x==1:
            return y == 1
        pow = 1
        while pow < y:
            pow = pow*x
        return pow == y
        