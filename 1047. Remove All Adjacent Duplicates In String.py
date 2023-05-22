class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [s[0]]
        i = 1
        while i < len(s):
            if stack and s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
        return "".join(stack)
