class Solution:
    def kthLargest(self, arr, k):
        arr.sort(reverse=True)
        # num = []
        # for i in range(len(arr)):
        #     num.append(max(arr))
        #     arr.remove(max(arr))
        
        return arr[k-1]
        
        
        