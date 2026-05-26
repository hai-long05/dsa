"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque([root])

        while q:
            length = len(q)
            new = []
            for i in range(length):
                node = q.popleft()
                if node:
                    if i < length - 1:
                        node.next = q[0]
                    else:
                        node.next = None

                    new.append(node.left)
                    new.append(node.right)
            if new:
                q = deque(new)

        return root