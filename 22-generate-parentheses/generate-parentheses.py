class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(curr_arr, opening_cnt, closing_cnt):
            if len(curr_arr) == 2 * n:
                res.append(''.join(curr_arr))
                return

            if opening_cnt < n:
                curr_arr.append("(")
                dfs(curr_arr, opening_cnt + 1, closing_cnt)
                curr_arr.pop()

            if closing_cnt < opening_cnt:
                curr_arr.append(")")
                dfs(curr_arr, opening_cnt, closing_cnt + 1)
                curr_arr.pop()


        dfs([], 0, 0)
        return res