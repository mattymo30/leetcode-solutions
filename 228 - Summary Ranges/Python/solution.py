class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        arr = "->"
        ans = []
        i = 0
        n = len(nums)
        while i < n:
            first_num = nums[i]
            count = 1
            last_num = first_num
            i += 1
            while  i < n and nums[i] == (last_num + 1):
                count += 1
                last_num = nums[i]
                i += 1

            if count == 1:
                ans.append(str(first_num))
                continue
            
            str_int = str(first_num) + arr + str(last_num)
            ans.append(str_int)

        return ans
