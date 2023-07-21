class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res, hashmap = [], {}
        count = 0
        for i in range(len(strs)):
            curr = ''.join(sorted(strs[i]))
            if curr in hashmap:
                res[hashmap[curr]].append(strs[i])
            else:
                hashmap[curr] = count
                res.append([strs[i]])
                count += 1
        return res
