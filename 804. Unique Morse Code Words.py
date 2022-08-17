class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        letters = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19,"u":20, "v":21, "w":22, "x":23, "y":24, "z": 25}
        array = []
        
        for i in words:
            string = ""
            for j in i:
                string += code[letters[j]]
            array.append(string)
        
        
        obj = {}
        count = 0
        for i in array:
            if i not in obj:
                obj[i] = i
                count += 1
        
        return count
        
