class Solution:
    def removeSpaces(self, s):
        l = []
        for ch in s:
            if ch!=" ":
                l.append(ch)
        st = "".join(l)
        
        return st