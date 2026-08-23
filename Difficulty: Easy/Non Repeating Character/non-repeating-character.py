# class Solution:
#     def nonRepeatingChar(self,s):
#         freq = {i:s.count(i) for i in s}
        
#         for i in s:
#             if freq[i] == 1:
#                 return i
            
#         return "$"
    
from collections import Counter
class Solution:
    def nonRepeatingChar(self, s):
        freq = Counter(s)

        for ch in s:
            if freq[ch] == 1:
                return ch

        return "$"
        