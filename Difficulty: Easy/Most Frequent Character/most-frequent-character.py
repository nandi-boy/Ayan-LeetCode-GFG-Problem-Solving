class Solution:
    def getMaxOccuringChar(self, s):
        freq = {c:s.count(c) for c in s}
        freq = dict(sorted(freq.items()))
        most = max(freq,key = freq.get)
        return most
        
        