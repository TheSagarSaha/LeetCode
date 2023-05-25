class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        c = Counter(s)
        count = 0
        while True:
            for i in target:
                if c[i] == 0:
                    return count
                c[i] -= 1
            count += 1
