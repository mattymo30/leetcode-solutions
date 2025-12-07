class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        left = 0
        right = len(s) - 1

        while left < right:
            left_word = s[left]
            right_word = s[right]
            s[left] = right_word
            s[right] = left_word
            left += 1 
            right -= 1
        return " ".join(s)
