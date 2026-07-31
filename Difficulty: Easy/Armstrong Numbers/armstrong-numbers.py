class Solution:
    def armstrongNumber (self, n):
        org = n
        nod = len(str(n))
        c=0
        while n>0:
            d=n%10
            c=c+(d**nod)
            n=n//10
        if org == c :
            return True
        