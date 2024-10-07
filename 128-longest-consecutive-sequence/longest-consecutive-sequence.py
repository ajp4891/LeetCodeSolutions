class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        track = set(nums)
        visited = set()
        mxseq = 0
        for n in track:
            if n not in visited:
                visited.add(n)
                front = back = n
                flagf = flagb = False
                seq = 1
                while True:
                    if not flagf:
                        front += 1
                        if front not in visited and front in track:
                            seq += 1
                            visited.add(front)
                        else:
                            flagf = True

                    if not flagb:
                        back -= 1
                        if back not in visited and back in track:
                            seq += 1
                            visited.add(back)
                        else:
                            flagb = True

                    if flagb and flagf:
                        break
                
            if seq > mxseq:
                mxseq = seq

        return mxseq