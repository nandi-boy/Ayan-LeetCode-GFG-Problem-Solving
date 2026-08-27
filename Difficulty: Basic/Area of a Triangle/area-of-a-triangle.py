import math
class Solution:
    def findArea(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            return 0.0
        s = (a+b+c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        return math.floor(area * 1000) / 1000
        