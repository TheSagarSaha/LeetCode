class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)
        arr = []
        for i in nums1:
            if i in nums2 or i in nums3:
                arr.append(i)
        for i in nums2:
            if i in nums1 or i in nums3:
                arr.append(i)
        for i in nums3:
            if i in nums1 or i in nums2:
                arr.append(i)
        return set(arr)
