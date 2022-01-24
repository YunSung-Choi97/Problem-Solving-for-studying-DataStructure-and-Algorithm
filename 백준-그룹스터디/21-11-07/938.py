from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        ret = 0

        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ret += node.val
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        
        return ret

# root = [10,5,15,3,7,13,18,1,None,6]
# low = 6
# high = 10

# root = [10, 5, 15, 3, 7, None, 18]
# low = 7
# high = 15

# Solution().rangeSumBST(root, low, high)