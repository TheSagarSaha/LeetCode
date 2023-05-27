class Solution:
    def isValid(self, s: str) -> bool:
        prev = None
        while s != "" and s != prev:
            prev = s
            s = s.replace("abc", "")
        return s == ""

# class Solution:
#     def isValid(self, s: str) -> bool:
#         string = []
#         for i in range(len(s)):
#             if s[i] == "a":
#                 string = string[:i] + list("abc") + string[i:]
#         return s == "".join(string)
