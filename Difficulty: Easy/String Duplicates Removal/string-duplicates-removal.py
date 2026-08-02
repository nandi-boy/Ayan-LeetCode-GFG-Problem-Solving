class Solution:
    def removeDuplicates(self, s):
	    seen = []
	    st = ""
	    for i in s:
	        if i not in seen:
	            seen.append(i)
	            st = st+i
	    return st

	    