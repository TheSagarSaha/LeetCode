# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res, level = [], 1
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
                if level % 2 != 0:
                    res.append(subarray)
                else:
                    res.append(subarray[::-1])
            level += 1
        return res
