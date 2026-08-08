class Solution:
    def intersection(self, arr1, arr2):
        s = set(arr2)
        res = set()

        for i in arr1:
            if i in s:
                res.add(i)

        return sorted(res)