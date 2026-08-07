class Solution:
    def middle(self, a, b, c):
        arr = []
        arr.append(a)
        arr.append(b)
        arr.append(c)
        arr.sort()
        return arr[1]
        
