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
        cur = head 
        
        while cur:
            # if the cur val & next val same
            while cur.next and cur.next.val == cur.val:
                # delete
                cur.next = cur.next.next
            cur = cur.next 
        return head