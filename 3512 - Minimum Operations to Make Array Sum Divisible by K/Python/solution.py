class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        num_sum = 0
        for n in nums:
            num_sum += n
        
        return num_sum % k
