class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        ans = 1
        if len(s) <= 1:
            return ans

        seen = set()

        def backtrack(start, seen):
            if start == len(s):
                return 0

            maxcnt = 0
            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if sub not in seen:
                    seen.add(sub)
                    maxcnt = max(maxcnt, 1 + backtrack(end, seen))
                    seen.remove(sub)

            return maxcnt
        return backtrack(0, seen)