class Solution:
    def removeDuplicates(self, arr):
        seen = set()
        
        for i in range(len(arr)):
            if arr[i] not in seen:
                seen.add(arr[i])
        arr = list(seen)
        arr.sort()
        return arr
        