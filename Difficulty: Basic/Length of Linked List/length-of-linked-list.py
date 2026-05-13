'''
Definition for Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def getCount(self, head):
        count = 0 
        if not head :
            return count
        curr = head
        while curr:
            curr = curr.next
            count = count+1
        return count