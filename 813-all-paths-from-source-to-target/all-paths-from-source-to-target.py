class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        d = defaultdict(set)

        target = len(graph) - 1
        res = []
        q = deque()
        q.append([0])

        while q:
            temp = q.popleft()
            if temp[-1] == target:
                res.append(temp)
            
            for nei in graph[temp[-1]]:
                q.append(temp + [nei])

        return res