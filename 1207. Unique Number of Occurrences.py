class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        d = {}
        for i in c:
            if c[i] in d:
                return False
            d[c[i]] = i
        return True
