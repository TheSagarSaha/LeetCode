class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(nums)
        index = nums.index(m)
        nums = set(nums)       
        nums.remove(m)
        for i in nums:
            if i*2 > m:
                return -1
        return index
