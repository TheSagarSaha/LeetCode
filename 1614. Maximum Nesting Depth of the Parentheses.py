class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        res = 0
        for i in s:
            if i == "(":
                stack.append("(")
                res = max(res, len(stack))
            elif i == ")":
                stack.pop()
        return res
