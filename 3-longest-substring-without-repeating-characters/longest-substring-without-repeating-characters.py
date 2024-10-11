class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = {}

        l, r = 0, 0
        ln = 1
        while r < len(s):
            if s[r] in seen:
                l = max(l, seen[s[r]] + 1)
            ln = max(ln, r - l + 1)
            seen[s[r]] = r
            r += 1

        return ln