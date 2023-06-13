class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        nonZero = set(nums+[0])
        nonZero.remove(0)
        while nonZero:
            m = min(nonZero)
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] -= m
            nonZero = set(nums)
            nonZero.remove(0)
            count += 1
        return count
