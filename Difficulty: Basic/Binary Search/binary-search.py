class Solution:
    def binarySearch(self, arr, k):
        l = 0
        h = len(arr)-1
        while l<=h:
            mid = (l+h)//2
            if k == arr[mid]:
                return True
            elif k < arr[mid]:
                h = mid-1
            elif k > arr[mid]:
                l = mid+1
        else:
            return False
        