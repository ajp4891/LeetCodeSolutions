class Solution:
    def sameEndSubstringCount(self, s: str, queries: list[list[int]]) -> list[int]:
        prefix = [[0] * 26]
        for c in s:
            prefix.append(prefix[-1].copy())
            prefix[-1][ord(c) - ord('a')] += 1
        res = []
        for left,right in queries:
            total = 0
            freq_left = prefix[left]
            freq_right = prefix[right+1] 
            for i in range(26):
                diff = freq_right[i] - freq_left[i]
                total += diff * (diff +1) //2
            res.append(total)
        return res