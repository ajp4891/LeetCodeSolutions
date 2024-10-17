class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        heap = []

        for i in range(n):
            t = temperatures[i]
            while heap and t > heap[-1][0]:
                _, ind = heap.pop()
                ans[ind] = i - ind
            heap.append((t, i))

        return ans