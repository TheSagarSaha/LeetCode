class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.lower()
        title = title.split()
        res = ""
        for i in title:
            if len(i) > 2:
                res += i.title()
            else:
                res += i
            res += " "
        return res[:len(res)-1]
