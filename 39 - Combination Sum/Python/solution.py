class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res, curr_sol = [], []
        num_cands = len(candidates)

        def backtracking(i, curr_sum):
            if curr_sum == target:
                res.append(curr_sol[:])
                return
            # need to exit
            if i == num_cands or curr_sum > target:
                return
            
            # can choose to not include this num
            backtracking(i+1, curr_sum)

            # choose to include this num, append and continue
            num = candidates[i]
            curr_sol.append(num)
            backtracking(i, curr_sum + num)
            curr_sol.pop()
        
        backtracking(0, 0)
        return res
