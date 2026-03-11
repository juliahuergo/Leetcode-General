# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        #Implementation: Reverse second half and then check for equality of halves
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        #slow is now in the middle of the list
        #reverse second half
        
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        print(prev.val)

        #compare if both halves are equal
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        
        return True
        
        
