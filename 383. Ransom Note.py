from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        res = ""
        string = Counter(magazine)

        for i in ransomNote:
            if i not in string or string[i] == 0:
                return False
            else:
                res += i
                string[i] -= 1
        return True
