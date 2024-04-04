# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        for _ in range(n):
            if right is None:
                return None
            right = right.next
            
        while right:
            left = left.next
            right = right.next
        
        # delete node
        left.next = left.next.next
        return dummy.next