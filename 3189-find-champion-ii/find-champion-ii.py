class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        countset = set([i for i in range(n)])

        for w, l in edges:
            if l in countset:
                countset.remove(l)
            

        return -1 if len(countset) > 1 else countset.pop()