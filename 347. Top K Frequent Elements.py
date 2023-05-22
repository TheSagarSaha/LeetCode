class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        c = c.most_common()
        arr = []
        for i in range(k):
            arr.append(c[i][0])
        return arr
