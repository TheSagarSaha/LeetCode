class Solution:
    def checkString(self, s: str) -> bool:
        if "b" not in s or "a" not in s:
            return True
        b = s.index("b")
        bStr = s[b:]
        if "a" in bStr:
            return False
        return True
