class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        d = {}
        ans = 1
        l, r = 0, 0

        while r < len(s):
            if s[r] in d and d[s[r]] + 1 > l:
                l = d[s[r]] + 1
            
            if ans < r - l + 1:
                ans = r - l + 1
            
            d[s[r]] = r
            r += 1

        return ans