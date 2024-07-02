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
        #   A -> B -> C -> D
        # P C    N
        
        prev = None 
        cur = head
        
        while cur:
            # save the next before breaking cur's pointer
            next = cur.next
            # reverse cur's pointer back to prev
            cur.next = prev
            prev = cur
            cur = next 
            
        return prev