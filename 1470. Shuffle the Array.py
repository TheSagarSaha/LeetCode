class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        x = n
        for i in range(n):
            arr.append(nums[i])
            arr.append(nums[x])
            x += 1
        return arr
    
