class Solution(object):
    def majorityElement(self, nums):
        # dict = {}
        # threshold = len(nums)//2
        # for i in nums:
        #     if i in dict :
        #         dict[i]+=1
        #     else :
        #         dict[i] = 1
                
        #     if dict[i] > threshold :
        #         return i
        candidate = None
        count = 0
        for i in nums :
            if count == 0:
                candidate = i
                count = 1
            elif candidate == i:
                count+=1
            else:
                count -= 1
            
        return candidate