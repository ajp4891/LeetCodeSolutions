class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        b, s = [], []

        for price, amt, typ in orders:
            if typ:
                heapq.heappush(s, (price, amt))
            else:
                heapq.heappush(b, (-price, amt))

            while b and s and -b[0][0] >= s[0][0]:
                (bprice, bamt), (sprice, samt) = heapq.heappop(b), heapq.heappop(s)
                if bamt > samt:
                    heapq.heappush(b, (bprice, bamt - samt))
                elif bamt < samt:
                    heapq.heappush(s, (sprice, samt - bamt))

        return sum(amt for _, amt in b + s) % (10**9 + 7)
        