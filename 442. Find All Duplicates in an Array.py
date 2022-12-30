class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        arr = []
        for i in c:
            if c[i] == 2:
                arr.append(i)
        return arr
