class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n < 1:
            return False
        else:
            res = 1

            while(res <= n):
                
                if(res == n):
                    return True
                else:
                    res *= 2
        
        return False
                
        
            
