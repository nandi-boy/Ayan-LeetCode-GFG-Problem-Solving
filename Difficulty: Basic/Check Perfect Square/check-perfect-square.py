import math
class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        a = math.sqrt(n)
        if a == int(a):
            return True
        else:
            return False
            