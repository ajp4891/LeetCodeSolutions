class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []

        if not digits:
            return ans
        dialer = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        def dfs(i, curr):
            if i == len(digits) == len(curr):
                ans.append(''.join(curr))
                return
            
            dials = dialer[digits[i]]
            for c in dials:
                curr.append(c)
                dfs(i + 1, curr)
                curr.pop()

            return

        dfs(0, [])
        return ans