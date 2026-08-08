class Solution:
    def factorial(self,n):
        if n==0 or n==1:
            return 1
        else:
            return n*self.factorial(n-1)
    def nPr(self, n: int, r: int) -> int:
        npr = self.factorial(n)//self.factorial(n-r)
        return npr
        