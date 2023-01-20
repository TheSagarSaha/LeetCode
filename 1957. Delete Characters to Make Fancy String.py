class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) <= 2:
            return s
        
        res = s[:2]
        for i in range(2, len(s)):
            if not (s[i] == s[i-1] == s[i-2]):
                res += s[i]

        return res
            
