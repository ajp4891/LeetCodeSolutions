class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            # print(t, t.isdigit(), len(t) > 1, stack)
            if t.isdigit() or len(t) > 1:
                stack.append(int(t))

            else:
                if len(stack) > 1:
                    second = stack.pop()
                    first = stack.pop()
                    ans = 0
                    if t == "+":
                        ans = first + second
                    elif t == "-":
                        ans = first - second
                    elif t == "*":
                        ans = first * second
                    elif t == "/":
                        ans = abs(first) // abs(second)
                        if ans != 0 and (first < 0 or second < 0) and not (first < 0 and second < 0):
                            ans = -ans
                    
                    stack.append(ans)

        return stack.pop()