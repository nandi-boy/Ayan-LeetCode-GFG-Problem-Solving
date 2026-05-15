#User function Template for python3
from collections import deque
class Solution:
    def firstNegInt(self, arr, k): 
        ans =[]
        queue = deque ()
        for i in range(k):
                if arr[i]<0:
                    queue.append(i)
        if queue:
            ans.append(arr[queue[0]])
        else:
            ans.append(0)
        for i in range(k,len(arr)):
            while queue and queue[0]<=i-k:
                queue.popleft()
            if arr[i]<0:
                    queue.append(i)
            if queue:
                ans.append(arr[queue[0]])
            else:
                ans.append(0)
        return ans
