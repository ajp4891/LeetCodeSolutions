class Solution:
    def minimizedMaximum(self, n, quantities):
        m = len(quantities)

        q = [(-q, q, 1) for q in quantities]

        heapq.heapify(q)

        for _ in range(n - m):
            (
                neg_ratio,
                total_q,
                curr_assigned_stores,
            ) = heapq.heappop(q)

            new_total_stores = curr_assigned_stores + 1
            new_ratio = total_q / new_total_stores

            heapq.heappush(
                q,
                (
                    -new_ratio,
                    total_q,
                    new_total_stores,
                ),
            )

        _, total_q, total_stores = heapq.heappop(
            q
        )

        return math.ceil(total_q / total_stores)