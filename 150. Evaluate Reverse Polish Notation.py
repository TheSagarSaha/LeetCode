class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.append(i)
            else:
                string = str(stack.pop(-2)) + str(i) + str(stack.pop(-1))
                stack.append(int(eval(string)))
        
        return int(stack[0])
