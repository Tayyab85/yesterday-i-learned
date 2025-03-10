"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        b = []
        for child in root.children:
            b.extend(self.postorder(child))
        b.append(root.val)
        return b