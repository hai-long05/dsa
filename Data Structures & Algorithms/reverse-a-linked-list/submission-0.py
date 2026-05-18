# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return None
        result = ListNode(head.val)
        head = head.next

        while head:
            tmp = ListNode(head.val)

            head = head.next
            tmp.next = result
            result = tmp

        return result