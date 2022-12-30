class Solution:
    def findGCD(self, nums: List[int]) -> int:
        M, m = max(nums), min(nums)
        res = 1
        for i in range(1, m+1):
            if m%i == 0 and M%i == 0:
                res = i
        return res
