class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = list(" " * len(s))
        for i in range(len(s)):
            res[indices[i]] = s[i]
        print(res)
        return "".join(res)
