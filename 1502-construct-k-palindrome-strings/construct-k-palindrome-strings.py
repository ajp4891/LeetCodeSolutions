class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        if len(s) == k:
            return True

        freq = [0] * 26
        odds = 0

        for c in s:
            freq[ord(c) - ord('a')] += 1

        for cnts in freq:
            if cnts % 2 == 1:
                odds += 1

        return odds <= k