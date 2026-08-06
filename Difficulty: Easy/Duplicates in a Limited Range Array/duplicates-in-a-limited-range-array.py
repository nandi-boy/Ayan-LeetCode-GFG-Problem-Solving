class Solution:
    def findDuplicates(self, arr):
        seen = set()
        ar = []
        for i in arr:
            if i in seen:
                ar.append(i)
            else:
                seen.add(i)
        return ar
        
        