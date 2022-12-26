from collections import Counter
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        a = Counter(s[:int(len(s)/2)])
        b = Counter(s[int(len(s)/2):])
        return (a["a"] + a["e"] + a["i"] + a["o"] + a["u"]) == (b["a"] + b["e"] + b["i"] + b["o"] + b["u"])
        
