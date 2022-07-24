class Solution(object):
    def twoSum(self, nums, target):
        obj = {}
        ans = [0, 0]
        for ind, element in enumerate(nums):
            find = target - element
            if find in obj:
                return [obj[find], ind]
            obj[element] = ind
            
