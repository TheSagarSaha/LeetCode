class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        res = []
        for i in c:
            if c[i] == 1:
                res.append(i)
        if len(res) < k:
            return ""
        return res[k-1]
