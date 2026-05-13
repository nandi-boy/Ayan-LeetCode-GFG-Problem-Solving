'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        if not head:
            return None
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast :
                count = 1
                fast = fast.next
                
                while slow != fast:
                    fast = fast.next
                    count = count+1
                return count
        return 0