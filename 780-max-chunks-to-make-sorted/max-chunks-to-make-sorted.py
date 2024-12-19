class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        prefix_max = arr[:]
        suffix_min = arr[:]

        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], prefix_max[i])

        print(prefix_max)

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], suffix_min[i])

        print(suffix_min)

        chunks = 0
        for i in range(n):
            if i == 0 or suffix_min[i] > prefix_max[i - 1]:
                chunks += 1

        return chunks