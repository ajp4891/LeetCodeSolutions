class Solution:
    def reorganizeString(self, s: str) -> str:
        cnts = defaultdict(int)
        for c in s:
            cnts[c] += 1

        maxheap = [(-freq, char) for char, freq in cnts.items()]
        heapq.heapify(maxheap)

        res = []

        while len(maxheap) > 1:
            f1, c1 = heapq.heappop(maxheap)
            f2, c2 = heapq.heappop(maxheap)

            res.extend([c1, c2])
            if f1 + 1 < 0:
                heapq.heappush(maxheap, (f1 + 1, c1))
            if f2 + 1 < 0:
                heapq.heappush(maxheap, (f2 + 1, c2))

        if maxheap:
            f, c = heapq.heappop(maxheap)
            if -f > 1:
                return ""
            res.append(c)

        return "".join(res)