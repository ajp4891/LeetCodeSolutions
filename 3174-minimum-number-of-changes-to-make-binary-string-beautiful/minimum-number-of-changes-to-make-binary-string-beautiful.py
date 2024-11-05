class Solution:
    def minChanges(self, s: str) -> int:
        i1 = 0
        i2 = 1
        min_changes = 0
        while i2 < len(s):
            if s[i1] != s[i2]:
                min_changes += 1

            i1 += 2
            i2 += 2

        return min_changes