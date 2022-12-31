class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        code = ""
        s = set()
        s.add(" ")
        for i in key:
            if i not in s:
                code += i
                s.add(i)
        res = ""
        for i in message:
            if i == " ":
                res += " "
            else:
                index = code.index(i)
                res += alphabet[index]
        return res
