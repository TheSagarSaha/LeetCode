class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        seq = [0, 1, 1]
        for i in range(3, n+1):
            seq.append(seq[i-1] + seq[i-2] + seq[i-3])
        return seq[-1]
