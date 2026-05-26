"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        def dfs(curr):
            if not curr:
                return curr
            
            for c in curr.children:
                dfs(c)

            result.append(curr.val)
        dfs(root)
        return result