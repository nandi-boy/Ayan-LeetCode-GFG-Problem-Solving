class Solution:
    def checkDivisibleBy36(self, s):
        digit_sum = 0
        for i in s:
            digit_sum = digit_sum+int(i)
            
        div_9 = (digit_sum%9 == 0)
        
        last_two = 0
        if len(s) == 1:
            last_two = int(s)
        else:
            last_two = int(s[-2:])
        
        div_4 = (last_two %4 == 0)
        
        return (div_9 and div_4)
            
        