class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr = sorted(set(nums))
        for i in range(len(arr)):
            nums[i] = arr[i]
        return len(arr)
        