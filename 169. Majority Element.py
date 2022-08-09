class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = len(nums) // 2
        count = 0
        element = 0
        for i in nums:
            if count == 0:
                count += 1
                element = i
            
            elif element == i:
                count += 1
            
            else:
                count -= 1
            
            
            if count > target:
                return element
        
        return element
    
