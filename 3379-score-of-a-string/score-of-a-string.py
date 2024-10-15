class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        prev = s[0]

        for c in s[1:]:
            total += abs(ord(c) - ord(prev))
            prev = c

        return total