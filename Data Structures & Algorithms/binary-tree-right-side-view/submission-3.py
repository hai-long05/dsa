# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        q = deque([root])

        while q:
            l = len(q)
            right = None
            for _ in range(l):
                n = q.popleft()
                if n:
                    right = n.val
                    q.append(n.left)
                    q.append(n.right)

            if right:
                result.append(right)

        return result