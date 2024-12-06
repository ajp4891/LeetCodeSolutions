class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        pool = list(i for i in range(1, n + 1) )
        bannedSet = set(banned)

        ans = 0

        for i in range(1, n + 1):
            if i in bannedSet:
                continue
            maxSum -= i
            if maxSum < 0:
                break

            ans += 1

        return ans