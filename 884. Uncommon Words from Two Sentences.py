class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1, s2 = s1.split(), s2.split()
        s1 = Counter(s1)
        s2 = Counter(s2)
        arr = []
        for i in s1:
            if (s1[i] == 1 and s2[i] == 0) or (s1[i] == 0 and s2[i] == 1):
                arr.append(i)
        for i in s2:
            if (s1[i] == 1 and s2[i] == 0) or (s1[i] == 0 and s2[i] == 1):
                arr.append(i)
        return arr        
