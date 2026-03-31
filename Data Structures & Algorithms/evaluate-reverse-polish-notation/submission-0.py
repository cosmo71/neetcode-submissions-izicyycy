class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for s in tokens:
            print(stack)

            if s == '+':
                stack.append(stack.pop() + stack.pop())

            elif s == '-':
                a = stack.pop()
                b = stack.pop()

                stack.append(b-a)

            elif s == '*':
                stack.append(stack.pop() * stack.pop())
            elif s == '/':
                a = stack.pop()
                b = stack.pop()

                stack.append(int(b/a))

            else:
                stack.append(int(s))
            
        return stack.pop()