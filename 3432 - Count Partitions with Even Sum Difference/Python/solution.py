class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        num_partitions = 0
        left_sum = 0
        right_sum = sum(nums)

        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum -= nums[i]
        
            if (left_sum - right_sum) % 2 == 0:
                num_partitions += 1
        return num_partitions
