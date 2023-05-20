class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        i = 0
        count = 0
        while i < len(s):
            if i+k < len(s):
                res.append(s[i:i+k])
                i += k
            else:
                string = s[i:]
                res.append(string + fill*(k-len(string)))
                break
        return res
