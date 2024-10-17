class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        heap = [(temperatures[0], 0)]

        for i in range(1, n):
            t = temperatures[i]
            while heap and t > heap[0][0]:
                _, ind = heapq.heappop(heap)
                ans[ind] = i - ind

            heapq.heappush(heap, (t, i))

        return ans