class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0
        for i in sentences:
            string = i.split()
            if len(string) >= count:
                count = len(string)
        
        return count
