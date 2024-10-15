class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        av = (sum(skill) / len(skill)) * 2
        ans = -1
        print(av * 2)
        if not av.is_integer():
            return ans


        groups = []
        tmp = defaultdict(int)
        for s in skill:
            comp = abs(av - s)
            if comp not in tmp:
                tmp[s] += 1
            else:
                tmp[comp] -= 1
                if tmp[comp] == 0:
                    del tmp[comp]
                groups.append(s * comp)
                print(s, comp)
        if tmp:
            return ans
        return int(sum(groups))