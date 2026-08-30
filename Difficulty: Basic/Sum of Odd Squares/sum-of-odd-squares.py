class Solution:
    def sumofodd(self, n: int) -> int:
        l =[]
        for i in range(1,2*n):
            if i%2 != 0:
                l.append(i)
        s = 0
        for i in l:
            s = s + ((i)**2)
        return s
        