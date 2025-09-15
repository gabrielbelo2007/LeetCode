from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0  # Inicializa o diâmetro máximo como zero
        self.depth(root)
        return self.diameter

    def depth(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        
        left_depth = self.depth(node.left)
        right_depth = self.depth(node.right)
        
        self.diameter = max(self.diameter, left_depth + right_depth)

        return 1 + max(left_depth, right_depth)