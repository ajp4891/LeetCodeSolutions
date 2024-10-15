class Solution:
    def countKeyChanges(self, s: str) -> int:
        prev = s[0]
        total = 0
        for c in s[1:]:
            if prev.lower() != c.lower():
                prev = c
                total += 1

        return total