class Solution:
    def majorityElement(self, arr):
        dict = {}
        threshold = len(arr)//2
        for i in arr:
            if i in dict :
                dict[i]+=1
            else :
                dict[i] = 1
                
            if dict[i] > threshold :
                return i
        else :
            return -1
        