class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            match i:
                case _ if i.lstrip("-").isnumeric():
                    stack.append(int(i))
                    
                case "+":
                    stack.append(stack.pop() + stack.pop())

                case "-":
                    op2, op1 = stack.pop(), stack.pop()
                    stack.append(op1 - op2)

                case "*":
                    stack.append(stack.pop() * stack.pop())

                case "/":
                    op2, op1 = stack.pop(), stack.pop()
                    stack.append(int(op1 / op2))


        return stack[0]
