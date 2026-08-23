class Solution:
    def findFrequency(self, arr, x):
        freq = {i:arr.count(i) for i in arr}
        return freq.get(x,0)
        