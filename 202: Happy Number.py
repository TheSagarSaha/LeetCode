class Solution:
    def isHappy(self, n: int) -> bool:
            d = set()
            
            while True:
                res = 0
                for i in str(n):
                    res += int(i) * int(i)
                n = res

                if res == 1:
                    return True
                if res not in d:
                    d.add(res)
                else:
                    return False
