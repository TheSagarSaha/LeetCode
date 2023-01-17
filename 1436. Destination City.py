class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start, end = set(), set()
        for i in paths:
            start.add(i[0])
            end.add(i[1])
        
        for i in end:
            if i not in start:
                return i
