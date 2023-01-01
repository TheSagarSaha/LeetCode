class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1 = Counter(words1)
        words2 = Counter(words2)
        count = 0
        for i in words1:
            if i in words2 and words1[i] == 1 and words2[i] == 1:
                count += 1
        return count
