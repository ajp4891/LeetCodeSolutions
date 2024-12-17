class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        heap = [(-ord(c), cnt) for c, cnt in Counter(s).items()]
        heapq.heapify(heap)
        ans = []

        while heap:
            char_neg, cnt = heapq.heappop(heap)
            char = chr(-char_neg)
            dup_limit = min(cnt, repeatLimit)
            ans.append(char * dup_limit)

            if cnt > dup_limit and heap:
                next_char, next_cnt = heapq.heappop(heap)
                ans.append(chr(-next_char))
                if next_cnt > 1:
                    heapq.heappush(heap, (next_char, next_cnt - 1))
                heapq.heappush(heap, (char_neg, cnt - dup_limit))

        return ''.join(ans)