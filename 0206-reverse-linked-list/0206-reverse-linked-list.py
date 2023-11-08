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
        #   1 -> 2 -> 3 -> 4
        #P  C.   N
        
        cur = head
        prev = None
        
        while cur is not None:
            nxt = cur.next # save the next node
            cur.next = prev # reverse pointer
            prev = cur # update prev ptr
            cur = nxt # update cur ptr
        return prev