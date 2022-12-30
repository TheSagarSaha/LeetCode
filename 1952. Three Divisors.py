class Solution:
    def isThree(self, n: int) -> bool:
        count = 2
        m = n//2
        for i in range(2, m+1):
            if n%i == 0:
                count += 1
        return count==3
