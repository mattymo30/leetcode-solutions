class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            if nums[i] > 0:
                break
                
            curr_val = nums[i]
            left_idx = i + 1
            right_idx = len(nums) - 1

            while left_idx < right_idx:
                left = nums[left_idx]
                right = nums[right_idx]
                three_sum = curr_val + left + right
                if three_sum == 0:
                    ans.append([curr_val, left, right])
                    left_idx += 1
                    right_idx -= 1
                    while nums[left_idx] == left and left_idx < right_idx:
                        left_idx += 1
                    while nums[right_idx] == right and left_idx < right_idx:
                        right_idx -= 1
                elif three_sum > 0:
                    right_idx -= 1
                else:
                    left_idx += 1
        return ans



        
