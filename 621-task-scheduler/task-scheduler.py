class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        counts = Counter(tasks)
        heap = [-v for v in counts.values()]
        heapq.heapify(heap)
        ans = 0

        while heap:
            # cycle = n + 1
            # tmp = []
            # len_vals = len(heap)
            # task_count = 0
            # while cycle > 0 and heap:
            #     cfreq = -heapq.heappop(heap)
            #     if cfreq > 1:
            #         tmp.append(-(cfreq - 1))
            #     task_count += 1
            #     cycle -= 1

            # for x in tmp:
            #     heapq.heappush(heap, x)

            # ans += task_count if not heap else n + 1

            ## Ajays solution
            
            tmp = []
            len_vals = len(heap)
            cycle = n + 1
            task_cnt = 0
            for _ in range(cycle):
                if not heap:
                    break
                tval = heapq.heappop(heap) + 1
                task_cnt += 1
                if tval < 0:
                    tmp.append(tval)
            
            for item in tmp:
                heapq.heappush(heap, item)

            ans += task_cnt if not heap else cycle

        return ans