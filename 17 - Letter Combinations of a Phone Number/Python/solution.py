class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        dig_len = len(digits)
        ans, curr_sol = [], []

        def backtracking(i):
            if i == dig_len:
                ans.append("".join(curr_sol))
                return
            
            curr_num = digits[i]
            for c in num_letter_map[curr_num]:
                curr_sol.append(c)
                backtracking(i+1)
                curr_sol.pop()
        
        backtracking(0)
        return ans

        
