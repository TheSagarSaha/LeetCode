class Solution:
    def secondHighest(self, s: str) -> int:
        n = {"0","1","2","3","4","5","6","7","8","9"}
        res = set()
        for i in s:
            if i in n:
                res.add(int(i))
        if not res:
            return -1                
        res.remove(max(res))
        if not res:
            return -1
        return max(res)
