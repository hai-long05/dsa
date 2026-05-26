# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None

        while head:
            temp = ListNode(head.val)
            temp.next = dummy
            dummy = temp
            head = head.next

        return dummy