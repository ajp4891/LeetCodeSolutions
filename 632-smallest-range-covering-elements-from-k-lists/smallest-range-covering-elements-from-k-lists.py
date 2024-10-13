class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        

        # items = list(nums)
        # smallest = [0, float('inf')]

        # while True:
        #     indmax = 0
        #     currsmall = currmax = items[0][0]
        #     for i, n in enumerate(items):
        #         if not n:
        #             break
        #             # logic to calculate final range if any

        #         curr_ele = n[0]

        #         if currsmall > curr_ele:
        #             currsmall = curr_ele
        #             indmax = i

        #         if currmax < curr_ele:
        #             currmax = curr_ele

        #     if (currmax - currsmall) < (smallest[-1] - smallest[0]):
        #         smallest[0] = currsmall
        #         smallest[1] = currmax
        #         currsmallrange = currmax - currsmall

        #     items[indmax].pop(0)
        #     if not items[indmax]:
        #         break

        # return smallest
        pq = []
        max_val = float("-inf")
        range_start = 0
        range_end = float("inf")

        # Insert the first element from each list into the min-heap
        for i in range(len(nums)):
            heapq.heappush(pq, (nums[i][0], i, 0))
            max_val = max(max_val, nums[i][0])

        # Continue until we can't proceed further
        while len(pq) == len(nums):
            min_val, row, col = heapq.heappop(pq)

            # Update the smallest range
            if max_val - min_val < range_end - range_start:
                range_start = min_val
                range_end = max_val

            # If possible, add the next element from the same row to the heap
            if col + 1 < len(nums[row]):
                next_val = nums[row][col + 1]
                heapq.heappush(pq, (next_val, row, col + 1))
                max_val = max(max_val, next_val)

        return [range_start, range_end]

            