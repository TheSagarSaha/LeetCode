# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        tree = []
        def traverse(root):
            if not root:
                return
            
            tree.append(root.val)
            traverse(root.left)
            traverse(root.right)
        
        traverse(root)
        for i in range(len(tree)):
            root.val = tree[i]
            root.left = None
            if i+1 != len(tree):
                root.right = TreeNode()
            root = root.right
            
