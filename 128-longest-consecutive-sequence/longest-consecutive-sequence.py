class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        track = set(nums)
        if len(track) <= 1:
            return len(track)
        
        ans = set(nums)


        for n in track:
            if n-1 not in track and n+1 not in track:
                ans.remove(n)
        del track

        mxseq = 1
        while ans:
            front = back = ans.pop()
            flagf = flagb = False
            seq = 1
            while True:
                if not flagf:
                    front += 1
                    if front in ans:
                        ans.remove(front)
                        seq += 1
                    else:
                        flagf = True

                if not flagb:
                    back -= 1
                    if back in ans:
                        ans.remove(back)
                        seq += 1
                    else:
                        flagb = True

                if flagb and flagf:
                    break
                
            if seq > mxseq:
                mxseq = seq

        return mxseq