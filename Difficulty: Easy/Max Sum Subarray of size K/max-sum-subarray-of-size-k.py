class Solution:
    def maxSubarraySum(self, arr, k):
        current_sum = sum(arr[0:k])
        max_sum = current_sum
        for i in range(k,len(arr)):
            current_sum = current_sum+arr[i]-arr[i-k]
            max_sum = max(max_sum,current_sum)
        return max_sum
        