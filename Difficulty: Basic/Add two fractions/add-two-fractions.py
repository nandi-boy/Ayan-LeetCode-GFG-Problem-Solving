import math
class Solution:
    def addFraction(self, num1: int, den1: int, num2: int, den2: int) -> list[int]:
        def lcm(den1,den2):
            return (den1*den2)//math.gcd(den1,den2)
                
        lcm_value = lcm(den1, den2)
        
        numa = ((lcm_value // den1)*num1) + ((lcm_value // den2)*num2)
        divisor = math.gcd(numa,lcm_value)
        
        numa = numa // divisor
        lcm_value = lcm_value // divisor

        return [numa, lcm_value]
        