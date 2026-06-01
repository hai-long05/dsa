# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        result = []
        level = 0

        while q:
            size = len(q)
            level_nodes = []
            for _ in range(size):
                n = q.popleft()
                if n:
                    level_nodes.append(n.val)
                    q.append(n.left)
                    q.append(n.right)
            
            if level % 2:
                level_nodes = level_nodes[::-1]
            if level_nodes:
                result.append(level_nodes)
            level += 1

        return result