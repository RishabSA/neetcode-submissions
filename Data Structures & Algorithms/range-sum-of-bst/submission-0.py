# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        vals = []
        self.traversal(root, vals)
        return sum([val for val in vals if val >= low and val <= high])
        
    def traversal(self, node, vals: list[int]):
        if node:
            self.traversal(node.left, vals)
            vals.append(node.val)
            self.traversal(node.right, vals)