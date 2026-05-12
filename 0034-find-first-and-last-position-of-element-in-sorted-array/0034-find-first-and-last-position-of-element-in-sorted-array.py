class Solution(object):
    def searchRange(self, nums, target):
        def lowerbound():
            low = 0
            high = len(nums)-1
            lb = -1
            while (low<=high):
                mid = (low+high)//2
                if target==nums[mid]:
                    lb=mid
                    high=mid-1
                elif target > nums[mid]:
                    low = mid+1
                elif target < nums[mid]:
                    high = mid-1
            return lb

        def upperbound():
            low = 0
            high = len(nums)-1
            ub = -1
            while (low<=high):
                mid = (low+high)//2
                if target==nums[mid]:
                    ub=mid
                    low=mid+1
                elif target > nums[mid]:
                    low = mid+1
                elif target < nums[mid]:
                    high = mid-1
            return ub
        return [lowerbound(),upperbound()]


            