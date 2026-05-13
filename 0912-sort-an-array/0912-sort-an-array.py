class Solution(object):
    def sortArray(self, nums):
        def mergeSortedArray(arr1,arr2):
            i,j = 0,0
            result = []
            while i< len(arr1) and j<len(arr2):
                if arr1[i] <= arr2[j]:
                    result.append(arr1[i])
                    i=i+1
                else:
                    result.append(arr2[j])
                    j=j+1
                    
            if i!= len(arr1):
                    while i<len(arr1):
                        result.append(arr1[i])
                        i=i+1
                        
            if j!= len(arr2):
                    while j<len(arr2):
                        result.append(arr2[j])
                        j=j+1
            return result 

        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        leftArr=nums[:mid]
        rightArr=nums[mid:]
        left = self.sortArray(leftArr)
        right = self.sortArray(rightArr)
        return mergeSortedArray(left,right)
