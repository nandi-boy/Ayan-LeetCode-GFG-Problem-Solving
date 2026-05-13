class Solution(object):
    def majorityElement(self, nums):
        dict = {}
        threshold = len(nums)//2
        for i in nums:
            if i in dict :
                dict[i]+=1
            else :
                dict[i] = 1
                
            if dict[i] > threshold :
                return i
        