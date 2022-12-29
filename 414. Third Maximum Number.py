class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        absoluteMax = max(nums)
        nums.remove(absoluteMax)
        if len(nums) == 0:
            return absoluteMax
        
        secondMax = max(nums)
        nums.remove(secondMax)
        if len(nums) == 0:
            return absoluteMax
        
        return max(nums)
