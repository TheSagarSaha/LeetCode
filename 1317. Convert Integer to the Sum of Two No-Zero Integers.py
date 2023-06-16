class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a, b = 1, n-1
        while "0" in str(a) or "0" in str(b):
            a += 1
            b -= 1
        
        return [a, b]
        
