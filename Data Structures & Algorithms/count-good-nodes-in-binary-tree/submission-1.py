# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxx):
            if not root:
                return 0

            curr = 1 if root.val >= maxx else 0
            left = dfs(root.left, max(root.val, maxx))
            right = dfs(root.right, max(root.val, maxx))

            return curr + left + right

        return dfs(root, root.val)