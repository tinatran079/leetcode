# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #   1 -> 2 -> 3 -> 4 -> 5
        #                       P C    N
        
        # initialize prev node
        # cur = head of linked list
        # temp variable, next
        # have cur.next point to prev
        # update the pointers one to the right
        # repeat until end of list and return prev
        
        prev = None
        cur = head
        
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            
        return prev