class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allowed == set(allowed)
        for i in words:
            if i == allowed or i in allowed:
                count += 1
            else:
                add = True
                for j in i:
                    if j not in allowed:
                        add = False
                        break
                if add:
                    count += 1
        return count
