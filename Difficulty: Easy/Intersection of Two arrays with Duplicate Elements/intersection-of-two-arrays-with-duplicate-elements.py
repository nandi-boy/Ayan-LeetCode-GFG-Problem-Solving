class Solution:
    def intersect(self, a, b):
        a.sort()
        b.sort()
        s=set(b)
        res = set()
        for i in a:
            if i in s:
                res.add(i)
        
        return sorted(res)
