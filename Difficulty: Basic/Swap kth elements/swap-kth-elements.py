
class Solution:
    def swapKth(self, arr, k):
        left = k-1
        right  = len(arr)-k
        arr[left],arr[right] = arr[right],arr[left]
        return arr
        
        
