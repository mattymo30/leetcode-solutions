class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = sys.maxsize
        for s in strs:
            min_length = min(min_length, len(s))
        
        common_prefix = ""

        for i in range(min_length):
            next_char = strs[0][i]

            for s in strs:
                if s[i] != next_char:
                    return common_prefix
            common_prefix = common_prefix + next_char
        
        return common_prefix
