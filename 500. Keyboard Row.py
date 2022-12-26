from collections import Counter
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set("qwertyuiop")
        second = set("asdfghjkl")
        third = set("zxcvbnm")
        total = Counter("qwertyuiopasdfghjklasdfghjklzxcvbnmzxcvbnmzxcvbnm")
        d = {1: first, 2: second, 3: third}
        res = []
        c = 0
        
        for word in words:
            i = word.lower()
            current = set(i)
            starter = total[i[0]]
            add = True
            for j in current:
                if j not in d[starter]:
                    add = False
            if add:
                res.append(word)

        return res

