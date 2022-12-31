class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        res = list(" " * len(s))
        for i in s:
            res[int(i[-1])-1] = i[:len(i)-1]
        return " ".join(res)
