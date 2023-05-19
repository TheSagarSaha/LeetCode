class Solution:
    def partitionString(self, s: str) -> int:
        duplicate, string, res, i = set(), "", [], 0
    
        while i < len(s):
            if s[i] not in duplicate:
                string += s[i]
                duplicate.add(s[i])
            else:
                res.append(string)
                string=""
                duplicate = set()
                i -= 1
            i += 1
        res.append(string)

        return len(res)
