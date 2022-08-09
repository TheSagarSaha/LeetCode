# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not len(nums):
            return None
        
        node = TreeNode()
        val = nums[int(len(nums)/2)]
        node.val = val
        
        node.left = self.sortedArrayToBST(nums[:(len(nums)//2)])
        node.right = self.sortedArrayToBST(nums[len(nums)//2+1:])

        return node
    
