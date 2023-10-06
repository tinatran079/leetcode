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
        #   A -> B -> C -> D -> null
        #P  C    N
        
        cur = head
        prev = None
        
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            
        return prev
        