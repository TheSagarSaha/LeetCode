class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()
            firstMax = stones[-1]
            secondMax = stones[-2]

            if firstMax == secondMax:
                stones.pop()
                stones.pop()
            
            else:
                stones[-2] = stones[-1] - stones[-2]
                stones.pop()

        if len(stones) == 0:
            return 0
        return stones[0]
