class Solution:
    def reverse(self, x: int) -> int:
        is_neg = False
        INT32_MAX = 2**31 - 1
        INT32_MIN = -2**31

        if x < 0:
            is_neg = True
        
        if x == 0:
            return 0
        
        x = list(str(x))

        left_ptr = 0
        if is_neg:
            left_ptr += 1

        right_ptr = len(x) - 1

        while left_ptr < right_ptr:
            temp = x[left_ptr]
            x[left_ptr] = x[right_ptr]
            x[right_ptr] = temp

            left_ptr += 1
            right_ptr -= 1
 
        trailing_zero = True
        reverse = ""
        for char in x:
            if char == "-":
                reverse += char
            elif char == "0":
                if trailing_zero:
                    continue
                reverse += char
            else:
                reverse += char
                if trailing_zero:
                    trailing_zero = False 
        
        if int(reverse) < INT32_MIN or int(reverse) > INT32_MAX:
            return 0

        return int(reverse)
        
        
        
