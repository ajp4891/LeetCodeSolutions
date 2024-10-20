class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        if len(expression) == 1:
            return expression == "t"
        
        ops = {'&', '|', '!'}

        stack = []
        for e in expression:
            temp = set()
            if e == ')':
                op = None
                while stack:
                    x = stack.pop()
                    if x in ops:
                        op = x
                        break
                    temp.add(x)
                print(temp)
                if op == "&":
                    stack.append("f" if "f" in temp else "t")
                elif op == "|":
                    stack.append("t" if "t" in temp else "f")
                else:
                    stack.append("f" if "t" in temp else "t")

            else:
                stack.append(e)

        return stack[-1] == "t"