# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        nf = False
        while q:
            n = q.popleft()
            if n:
                if nf:
                    return False
                q.append(n.left)
                q.append(n.right)
            else:
                nf = True



        return True

                

                