class Solution:
    def reverseArray(self, arr):
        left_p = 0
        right_p = len(arr) - 1

        while left_p < right_p:
            arr[left_p], arr[right_p] = arr[right_p], arr[left_p]
            left_p += 1
            right_p -= 1