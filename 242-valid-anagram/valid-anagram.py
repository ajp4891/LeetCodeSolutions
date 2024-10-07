class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = dict()

        for l in s:
            if l not in d:
                d[l] = 0
            d[l] += 1

        for l in t:
            if l not in d or d[l] <= 0:
                return False
            else:
                d[l] -= 1
                if d[l] == 0:
                    del d[l]

        return not d