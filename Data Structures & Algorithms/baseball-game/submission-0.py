class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack =[]
        for i in operations:
            if len(stack) > 1 and i =='+':
                b = stack[-1]
                a = stack[-2]
                stack.append(b+a)
            elif len(stack)>=1 and  i == 'C':
                stack.pop()
            elif len(stack)>=1 and  i =='D':
                stack.append(int(stack[-1])*2) 
            else:
                stack.append(int(i))
        return sum(stack)
            
        