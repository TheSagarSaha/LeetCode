class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        d = set(nums)
        i = 1
        while True:
            if i not in d:
                return i
            i += 1
