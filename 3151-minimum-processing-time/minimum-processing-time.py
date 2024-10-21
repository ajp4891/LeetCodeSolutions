class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort(reverse=True)
        i = 0
        maxtime = 0
        while i < len(tasks):
            if i % 4 == 0:
                maxprocessortime = processorTime.pop()
            t = tasks[i]
            maxtime = max(t + maxprocessortime, maxtime)
            i += 1
        
        return maxtime