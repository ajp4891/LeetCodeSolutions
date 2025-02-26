class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        if len(s) == k:
            return True

        # freq = [0] * 26
        # odds = 0

        # for c in s:
        #     freq[ord(c) - ord('a')] += 1

        # for cnts in freq:
        #     if cnts % 2 == 1:
        #         odds += 1

        # return odds <= k
        odd_count = 0

        for chr in s:
            odd_count ^= 1 << (ord(chr) - ord("a"))
        return bin(odd_count).count("1") <= k