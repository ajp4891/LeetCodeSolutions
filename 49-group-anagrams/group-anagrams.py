class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            cnts = [0] * 26
            for c in s:
                cnts[ord(c) - ord('a')] += 1

            ans[tuple(cnts)].append(s)

        return ans.values()