class Solution:
    def countFreq(self, arr):
        freq ={}
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        res = []
        for key,value in freq.items():
            res.append([key,value])
        return res
            
            
        