class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openb = 0
        req = 0

        for c in s:
            if c == "(":
                openb += 1
            else:
                if openb > 0:
                    openb -= 1
                else:
                    req += 1

        return openb + req