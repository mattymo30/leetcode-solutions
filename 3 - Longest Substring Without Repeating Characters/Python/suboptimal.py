class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        left_ptr = 0
        right_ptr = 1

        while left_ptr <= len(s) - 1:
            max_possible_len = len(s) - left_ptr
            if longest >= max_possible_len:
                break
            curr_longest = 0
            left_char = s[left_ptr]
            seen.add(left_char)
            curr_longest += 1
            while right_ptr <= len(s) - 1:
                next_char = s[right_ptr]
                print(next_char)
                if next_char in seen:
                    break
                curr_longest += 1
                seen.add(next_char)
                right_ptr += 1
            
            if curr_longest > longest:
                longest = curr_longest
            left_ptr += 1
            right_ptr = left_ptr + 1
            seen = set()
        return longest
            
