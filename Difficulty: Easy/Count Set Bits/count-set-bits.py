class Solution:
    def setBits(self, n):
        binary = bin(n)[2:]
        l = [int(i) for i in str(binary) ]
        count = 0
        for j in l:
            if j==1:
                count+=1
        return count
            
