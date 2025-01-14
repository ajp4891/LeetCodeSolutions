class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        aset, bset = set(), set()
        current_cnt = 0
        ans = []
        for i in range(len(A)):
            if A[i] == B[i]:
                current_cnt += 1

            if A[i] in bset:
                current_cnt += 1

            if B[i] in aset:
                current_cnt += 1

            aset.add(A[i])
            bset.add(B[i])
            ans.append(current_cnt)

        return ans