#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
		ans = []
		def power_set(index, current_str):
            if index == len(s):
                if current_str: 
                    ans.append(current_str)
                return
            power_set(index+1,current_str+s[index])
            power_set(index+1,current_str)
        power_set(0,"")
        ans.sort()
        return ans