class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.split()
        text.sort(key=lambda item: len(item))
        text = " ".join(text)
        return text.capitalize()
    
        
