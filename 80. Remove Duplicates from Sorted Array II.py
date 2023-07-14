class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right, count = 0, 1, 1
        while left < right and len(nums) > right:
            if nums[left] == nums[right] and count == 2:
                nums[right] = "_"
                right += 1
            elif nums[left] == nums[right]:
                right += 1
                count += 1
            else:
                left = right
                right += 1
                count = 1
        res = 0

        index, pointer = 0, 0
        while index < len(nums):
            if nums[index] == "_":
                while pointer < len(nums)-1 and nums[pointer] == "_":
                    pointer += 1
                nums[index] = nums[pointer]
                nums[pointer] = "_"
            index += 1
            pointer = index
        
        res = 0
        for i in nums:
            if i == "_":
                break
            res += 1
        return res
