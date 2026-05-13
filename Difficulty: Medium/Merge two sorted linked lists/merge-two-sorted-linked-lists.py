'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self, head1, head2):
        
        Dummy = Node(0) 
        newDummy = Dummy
        
        while head1 and head2:    
            if head1.data <= head2.data:
                newDummy.next = head1
                head1 = head1.next
            else:
                newDummy.next = head2
                head2 = head2.next
            newDummy = newDummy.next
            
        if head1:
            newDummy.next = head1
        else:
            newDummy.next = head2
        return Dummy.next
            
            