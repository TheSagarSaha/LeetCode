class Solution:
    def firstUniqChar(self, s: str) -> int:
        found = {}
        for i in range(len(s)):
            newtext = s[i+1::]
            if s[i] not in newtext and s[i] not in found:
                return i
            found[s[i]] = i
        return -1
            
