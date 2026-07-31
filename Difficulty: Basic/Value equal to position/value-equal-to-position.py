class Solution:
    def valEqualToPos(self, arr):
        ar=[]
        for i in range (len(arr)):
            if arr[i] == i+1:
                ar.append(arr[i])
        return ar
        