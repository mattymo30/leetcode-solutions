class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        temp = [-1] * (n + 1)

        for num in nums:
            temp[num] = 1
        for i, t in enumerate(temp):
            if t == -1:
                return i
        
