class Solution:
    def quadraticRoots(self, a, b, c):
                if a==0:
                    return -1
                d = (b**2)-4*a*c
                if d>=0:
                    r1 = (-b + math.sqrt(d)) / (2*a)
                    r2 = (-b - math.sqrt(d)) / (2*a)
                    return [math.floor(r1),math.floor(r2)]
                if d<0:
                    return ["Imaginary"]
