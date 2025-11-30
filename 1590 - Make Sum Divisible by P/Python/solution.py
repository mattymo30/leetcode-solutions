class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        if total % p == 0:
            return 0

        rem = total % p
        if rem in nums:
            return 1
        
        curr_sum = 0
        min_len = len(nums)
        rem_dict = {
            0: -1
        }

        for i, num in enumerate(nums):
            curr_sum = (curr_sum + num) % p
            left = (curr_sum - rem + p) % p

            if left in rem_dict:
                min_len = min(min_len, i - rem_dict[left])
            
            rem_dict[curr_sum] = i

        if min_len == len(nums):
            return -1
        
        return min_len
        
