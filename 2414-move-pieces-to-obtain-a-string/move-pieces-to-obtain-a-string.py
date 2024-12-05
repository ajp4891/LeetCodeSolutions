class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        start_i, target_i = 0, 0

        while start_i < n or target_i < n:
            while start_i < n and start[start_i] == "_":
                start_i += 1

            while target_i < n and target[target_i] == "_":
                target_i += 1

            if start_i == n or target_i == n:
                return start_i == n and target_i == n

            if (
                start[start_i] != target[target_i]
                or (start[start_i] == 'R' and start_i > target_i)
                or (start[start_i] == 'L' and start_i < target_i)
            ):
                return False

            start_i += 1
            target_i += 1

        return True