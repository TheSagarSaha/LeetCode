# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            currLength = len(queue)
            subarray = []
            for i in range(currLength):
                node = queue.popleft()
                if node:
                    subarray.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if subarray:
                res.append(subarray)
        return res[-1][0]
