class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)
        res = []
        for i in c:
            if i == c[i]:
                res.append(i)
        if len(res) > 0:
            return max(res)
        return -1
