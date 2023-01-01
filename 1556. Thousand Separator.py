class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = [nums[0]]
        total = nums[0]
        for i in range(1, len(nums)):
            total += nums[i]
            arr.append(total)
        return arr
