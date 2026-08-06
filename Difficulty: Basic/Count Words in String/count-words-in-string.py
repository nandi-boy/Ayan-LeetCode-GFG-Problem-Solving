class Solution:
    def countWords(self,s):
        l = list(s.split())
        count = 0
        for i in range(len(l)):
            count+=1
        return count
        