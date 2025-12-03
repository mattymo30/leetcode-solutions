class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, curr_sol = [], []
        perm_len = len(nums)

        def backtracking():
            if len(curr_sol) == perm_len:
                ans.append(curr_sol[:])
                return
            
            for num in nums:
                if num not in curr_sol:
                    curr_sol.append(num)
                    backtracking()
                    curr_sol.pop()
        
        backtracking()
        return ans
