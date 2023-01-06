class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        c = Counter(s)
        res = set()
        for i in c:
            if c[i] not in res:
                res.add(c[i])
        return len(res) == 1
