class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        numset = list(set(nums))
        numset.sort()
        d = defaultdict(int)
        for n in numset:
            if not d or math.sqrt(n) not in d:
                d[n] = 1
            else:
                x = math.sqrt(n)
                d[n] = d[x] + 1
                del d[x]
        final = max(d.values())
        return final if final > 1 else -1