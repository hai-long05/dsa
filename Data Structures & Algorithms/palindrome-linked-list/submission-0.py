# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:    
        prev, curr = None, head
        while curr:
            reverse = ListNode(curr.val)
            reverse.next = prev
            prev = reverse
            curr = curr.next

        while head:
            if head.val != reverse.val:
                return False

            head = head.next
            reverse = reverse.next

        return True