# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque()
        queue.append(root)
        tree = []
        res = -1
        maximum = float(-inf)
        while queue:
            subarray = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    subarray.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if subarray:
                tree.append(subarray)

        for i in range(len(tree)):
            value = sum(tree[i])
            print(value, maximum)
            if value > maximum:
                maximum = value
                res = max(res, i)
        return res+1
