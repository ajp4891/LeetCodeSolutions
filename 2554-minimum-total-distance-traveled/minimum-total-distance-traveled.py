class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        factory_pos = []
        for f in factory:
            factory_pos.extend([f[0]] * f[1])

        rob_count = len(robot)
        fac_count = len(factory_pos)

        dp = [[None] * (fac_count + 1) for _ in range(rob_count + 1)]

        def calc_min_dis(rob_ind, fac_ind):
            if dp[rob_ind][fac_ind] is not None:
                return dp[rob_ind][fac_ind]

            if rob_ind == rob_count:
                dp[rob_ind][fac_ind] = 0
                return dp[rob_ind][fac_ind]

            if fac_ind == fac_count:
                dp[rob_ind][fac_ind] = int(1e12)
                return dp[rob_ind][fac_ind]

            assign = abs(
                robot[rob_ind] - factory_pos[fac_ind]
                ) + (
                    calc_min_dis(rob_ind + 1, fac_ind + 1)
                )

            skip = calc_min_dis(rob_ind, fac_ind + 1)
            dp[rob_ind][fac_ind] = min(assign, skip)

            return dp[rob_ind][fac_ind]

        return calc_min_dis(0, 0)