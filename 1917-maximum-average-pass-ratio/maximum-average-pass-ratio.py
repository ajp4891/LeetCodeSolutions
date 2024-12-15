class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def calc_gain_on_adding_student(passes, total_students):
            return (passes + 1) / (total_students + 1) - passes / total_students


        heap = []
        for passes, total_students in classes:
            gain = calc_gain_on_adding_student(passes, total_students)
            heapq.heappush(heap, (-gain, passes, total_students))

        for _ in range(extraStudents):
            curr_gain, passes, total_students = heapq.heappop(heap)
            heapq.heappush(
                heap,
                (
                    -calc_gain_on_adding_student(passes + 1, total_students + 1),
                    passes + 1,
                    total_students + 1
                )
            )

        total_pass_ratio = 0
        while heap:
            _, passes, total_students = heapq.heappop(heap)
            total_pass_ratio += passes/total_students

        return total_pass_ratio / len(classes)