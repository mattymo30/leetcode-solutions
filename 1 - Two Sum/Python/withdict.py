class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        num_of_nums = len(nums)

        for i in range(num_of_nums):
            curr_val = nums[i]
            rem = target - curr_val
            if curr_val in d:
                arr_1 = d.get(curr_val)
                return [arr_1, i]
            else:
                d[rem] = i
