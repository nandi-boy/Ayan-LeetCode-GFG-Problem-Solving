class Solution:
	def binaryToDecimal(self, b):
        decimal = 0
        
        for i in b:
            decimal = decimal*2 + int(i)
            
        return decimal
		