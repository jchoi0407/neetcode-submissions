class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for e in tokens:
            if e not in {"+", "-", "*", "/"}:
                stack.append(int(e))
            else:
                if e == "+":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(num1 + num2)
                elif e == "-":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(num1 - num2)
                elif e == "*":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(num1 * num2)
                else:
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(int(num1 / num2))
        
        return stack[0]
                    