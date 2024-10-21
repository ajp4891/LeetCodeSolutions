class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        i = 0
        maxtime = 0
        while i < len(tasks):
            # if i % 4 == 0:
            maxprocessortime = processorTime[i//4]
            maxtime = max(tasks[i] + maxprocessortime, maxtime)
            i += 4
        
        return maxtime