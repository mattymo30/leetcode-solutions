class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        while tokens:
            new = tokens.pop(0)
            if new == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif new == "-":
                second, first = int(stack.pop()), int(stack.pop())
                stack.append(first - second)
            elif new == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif new == "/":
                second, first = int(stack.pop()), int(stack.pop())
                div = first / second
                stack.append(div)
            else:
                stack.append(int(new))
            
        return int(stack[0])
