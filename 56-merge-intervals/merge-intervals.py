class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        final = [intervals[0]]

        for s, e in intervals[1:]:
            prev_e = final[-1][1]
            if s <= prev_e:
                if e > prev_e:
                    final[-1][1] = max(e, prev_e)
            else:
                final.append([s, e])
        
        return final

