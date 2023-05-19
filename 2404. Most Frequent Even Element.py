class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        hashmap = {}
        m = -1
        for i in nums:
            if i%2 == 0:
                if i not in hashmap:
                    hashmap[i] = 1
                else:
                    hashmap[i] += 1
                m = max(m, hashmap[i])
        
        if not hashmap:
            return -1
            
        ans = {}
        for i in hashmap:
            if hashmap[i] == m:
                ans[i] = m
        return min(ans)
