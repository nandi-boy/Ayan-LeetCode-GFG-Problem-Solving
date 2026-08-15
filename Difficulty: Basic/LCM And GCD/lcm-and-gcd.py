class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        # code here
        g = min(a,b)
        x,y = a,b
        lcm = 0
        gcd = 0
        for i in range (1,g+1):
            if x%i == 0 and y%i ==0:
                gcd = i
        lcm = (a*b) // gcd
        return [lcm,gcd]