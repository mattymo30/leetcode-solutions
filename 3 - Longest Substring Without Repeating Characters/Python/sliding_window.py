class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # starting pointers for the string
        seen = set()
        longest = 0
        left_ptr = 0

        for right_ptr in range(len(s)):
           # keep removing from seen until repeated char is gone
            while s[right_ptr] in seen:
                seen.remove(s[left_ptr])
                left_ptr += 1
            
            seen.add(s[right_ptr])
            longest = max(longest, right_ptr - left_ptr + 1)
        return longest
            
