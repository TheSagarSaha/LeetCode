# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, leftMargin, rightMargin):
            if not node:
                return True
            if not (node.val < rightMargin and node.val > leftMargin):
                return False
            
            return (valid(node.left, leftMargin, node.val) and valid(node.right, node.val, rightMargin))
        
        return valid(root, float("-inf"), float("inf"))
    
