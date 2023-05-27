class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = 0
        for i in c:
            if c[i] == 1:
                res += i
        return res
