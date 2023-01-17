class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = sorted(nums)
        if nums == n:
            return True
        elif nums == n[::-1]:
            return True
        return False
