# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        while head and head.val == val:
            head = head.next

        dummy = head
        prev = None
        while dummy:
            next_node = dummy.next
            if dummy.val == val:
                prev.next = next_node
                dummy = next_node
                if next_node:
                    next_node = next_node.next
                
            else:
                prev = dummy
                dummy = dummy.next
                if next_node:
                    next_node = next_node.next

        return head
