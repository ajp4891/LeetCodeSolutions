class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # openb = 0
        # req = 0

        # for c in s:
        #     if c == "(":
        #         openb += 1
        #     else:
        #         if openb > 0:
        #             openb -= 1
        #         else:
        #             req += 1

        # return openb + req
        need = 0 # number neede for ')'
        res = 0

        for p in s:
            if p == '(':
                need += 1
            
            if p == ')':
                need -= 1

                if need == -1:
                    res += 1
                    need = 0
        return res + need