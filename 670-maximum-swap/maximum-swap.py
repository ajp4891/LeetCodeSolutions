class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 10:
            return num

        numlist = list(str(num))
        n = len(numlist)
        max_right_ind = [0] * n
        max_right_ind[n - 1] = n - 1

        for i in range(n-2, -1, -1):
            max_right_ind[i] = (
                i if numlist[i] > numlist[max_right_ind[i + 1]]
                else max_right_ind[i + 1]
            )

        for i in range(n):
            if numlist[i] < numlist[max_right_ind[i]]:
                numlist[i], numlist[max_right_ind[i]] = numlist[max_right_ind[i]], numlist[i]
                return int(''.join(numlist))

        return num