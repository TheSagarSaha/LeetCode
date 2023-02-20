class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        seq = [0, 1]
        for i in range(2, n+1):
            seq.append(seq[i-1] + seq[i-2])
        return seq[-1]
