class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class Solution:
    def insertPos(self, head, pos, val):
        if pos == 1:
            newNode = Node(val)
            newNode.next = head
            return newNode
        curr = head

        for i in range(1, pos - 1):
            if curr is None:
                return head
            curr = curr.next

        if curr is None:
            return head

        newNode = Node(val)
        newNode.next = curr.next
        curr.next = newNode
        return head
        