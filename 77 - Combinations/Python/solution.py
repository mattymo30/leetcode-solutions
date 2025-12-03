class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans, curr_sol = [], []

        def backtracking(num):
            if len(curr_sol) == k:
                ans.append(curr_sol[:])
                return
            
            need = k - len(curr_sol)
            # allows us to ignore this num
            if num > need:
                backtracking(num-1)
            
            curr_sol.append(num)
            backtracking(num-1)
            curr_sol.pop()

        backtracking(n)
        return ans
        
