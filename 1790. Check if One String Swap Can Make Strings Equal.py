class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        arr = [] # Array Struct: [s1_first_typo, s2_first_type, s1_second_typo, s2_second_typo]
        count = 0
        for i in range(len(s1)):
            if count > 2:
                return False

            if s1[i] != s2[i]:
                arr.append(s1[i])
                arr.append(s2[i])
                count += 1

        if count > 2:
            return False
        if len(arr) == 2:
            return arr[0] == arr[1]
        return arr[0] == arr[3] and arr[1] == arr[2]
            
