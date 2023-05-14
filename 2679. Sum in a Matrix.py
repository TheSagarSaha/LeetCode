class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        ans = 0
        array = []
        while (len(nums[0])):
            for i in range(len(nums)):
                m = max(nums[i])
                nums[i].remove(m)
                array.append(m)
            ans += max(array)
            array = []
        return ans
