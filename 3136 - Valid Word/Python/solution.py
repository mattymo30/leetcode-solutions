class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        cons_count = 0
        vowel_count = 0

        vowels = "aeiou"
        for c in word:
            if c.isalpha():
                if c.lower() in vowels:
                    vowel_count += 1
                else:
                    cons_count += 1
            else:
                if not c.isdigit():
                    return False
        if cons_count == 0 or vowel_count == 0:
            return False
        return True

        
