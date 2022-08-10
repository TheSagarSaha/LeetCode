class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        dic = {}
        for i in nums1:
            if i in nums2 and i not in dic:
                arr.append(i)
                dic[i] = i
        return arr
    
