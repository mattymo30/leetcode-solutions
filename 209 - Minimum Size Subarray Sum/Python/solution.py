class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_nums = sys.maxsize
        left = right = 0
        summ = 0

        while right < len(nums):
            summ += nums[right]

            if summ < target:
                right += 1
            else:
                min_nums = min(min_nums, right - left + 1)
                summ -= nums[left]
                summ -= nums[right]
                left += 1

        if min_nums == sys.maxsize:
            return 0
        return min_nums
        
