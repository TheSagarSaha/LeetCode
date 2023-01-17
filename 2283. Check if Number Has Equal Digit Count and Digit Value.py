class Solution:
    def digitCount(self, num: str) -> bool:
        c = Counter(num)
        for i in range(len(num)):
            if int(num[i]) != int(c[str(i)]):
                return False
        return True
