class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                curr_longest = 1
                while num + curr_longest in nums:
                    curr_longest += 1
                longest = max(longest, curr_longest)

        return longest
        
