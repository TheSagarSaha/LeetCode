class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashmap = {}
        for i in range(len(heights)):
            hashmap[heights[i]] = names[i]
        s = sorted(hashmap)
        res = []
        for i in s:
            res.append(hashmap[i])
        return res[::-1]
