class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums = set(nums)
        while True:
            if original not in nums:
                return original
            original *= 2
