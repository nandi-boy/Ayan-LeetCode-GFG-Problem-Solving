class Solution:
	def find_fact(self, n):
		if n == 0:
		    return 1
		else:
		    return n*self.find_fact(n-1)
		