class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        word += "."
        vowels, curr, string = list("aeiou"), "", ""
        res, ans, counter = 0, 0, 0
        for i in range(len(word)):
            if not curr and word[i] == "a":
                curr = "a"
                counter += 1
                ans += 1
                string += "a"
            elif word[i] == curr:
                ans += 1
                string += word[i]
            elif counter < 5 and word[i] == vowels[counter]:
                counter += 1
                ans += 1
                curr = word[i]
                string += word[i]
            elif curr and word[i] == "a":
                if len(set(string)) == 5:
                    res = max(res, ans)
                ans, counter, curr, string = 1, 1, "a", "a"
            else:
                if len(set(string)) == 5:
                    res = max(res, ans)
                ans, counter, curr, string = 0, 0, "", ""

        return res
