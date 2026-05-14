'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteNode(self, head, x):
        curr = head
        pos = 1
        if not head:
            return None
        if x == 1:
            return head.next
            
        for i in range(1,x-1):
            curr = curr.next
        curr.next = curr.next.next
        return head
        
        
