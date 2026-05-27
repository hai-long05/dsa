# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        s, f = dummy, dummy.next
        while f:
            if f.val == val:
                f = f.next
            else:
                s.next = f
                s = s.next
                f = f.next 

        s.next = None

        return dummy.next
