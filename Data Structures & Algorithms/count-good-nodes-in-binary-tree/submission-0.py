# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(curr: TreeNode, max_value: int) -> int:
            if not curr: 
                return 0

            result = 1 if curr.val >= max_value else 0
            left = dfs(curr.left, max(curr.val, max_value))
            right = dfs(curr.right, max(curr.val, max_value))

            return result + left + right

        return dfs(root, root.val)