# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        values = set()
        prev = None
        current = head
        
        while current is not None:
            if current.val in values:
                prev.next = current.next
            else:
                values.add(current.val)
                prev = current
            current = current.next
        
        return head