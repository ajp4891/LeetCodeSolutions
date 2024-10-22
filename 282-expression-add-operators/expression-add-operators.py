class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def dfs(i, curnum, prevnum, string):
            if i == len(num):
                if curnum == target:
                    res.append(string)
                return

            for j in range(i, len(num)):
                if j > i and num[i] == '0':
                    break
                val = int(num[i:j + 1])

                if i == 0:
                    dfs(j + 1, curnum + val, val, string + str(val))
                else:
                    dfs(j + 1, curnum + val, val, string + "+" + str(val))
                    dfs(j + 1, curnum - val, -val, string + "-" + str(val))
                    dfs(j + 1, curnum - prevnum + prevnum * val, prevnum * val, string + "*" + str(val))

        dfs(0, 0, 0, "")
        return res