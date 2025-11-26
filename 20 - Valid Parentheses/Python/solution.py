class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_paren = "([{"
        parens = {")": "(", "}": "{", "]": "["}
        for p in s:
            # open paren, just add to stack
            if p in open_paren:
                stack.append(p)
            else:
                # pop top of stack
                if len(stack) == 0:
                    return False
                open_to_check = stack.pop()
                if parens[p] != open_to_check:
                    return False
        
        if len(stack) == 0:
            return True
        return False
