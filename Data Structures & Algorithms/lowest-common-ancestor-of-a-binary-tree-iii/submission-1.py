"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        nodes = set()

        while p:
            nodes.add(p)
            p = p.parent

        for n in nodes:
            if q in nodes:
                return q
            q = q.parent

        return q
        