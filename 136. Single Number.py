class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            temp = nums[i]
            del nums[i]
            if temp not in nums:
                return temp
            nums.insert(i, temp)
            
