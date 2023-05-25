class Solution:
    def isPathCrossing(self, path: str) -> bool:
        points = { (0, 0) }
        y, x = 0, 0
        for i in path:
            if i == "N":
                y += 1
            elif i == "E":
                x += 1
            elif i == "S":
                y -= 1
            else:
                x -= 1
            
            if (x, y) in points:
                return True
            points.add((x, y))
        return False
