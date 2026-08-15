class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if i == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)  
            elif i == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif i == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)
            elif i == '/':
                a = stack.pop()
                b = stack.pop()
                # int() truncates toward zero in Python (e.g., int(-0.33) becomes 0)
                stack.append(int(b / a))
            else:
                # It's a number, push it straight onto the stack
                stack.append(int(i))
                
        # The final remaining item is our total result
        return stack[0]