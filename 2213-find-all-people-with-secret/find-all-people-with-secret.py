class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])
        knows_secret = [False] * n
        knows_secret[0] = True
        knows_secret[firstPerson] = True

        same_time_meet_map = defaultdict(list)

        for p1, p2, t in meetings:
            same_time_meet_map[t].append((p1, p2))

        for time in same_time_meet_map:

            current_meet_map = defaultdict(list)
            q = set()
            for p1, p2 in same_time_meet_map[time]:
                current_meet_map[p1].append(p2)
                current_meet_map[p2].append(p1)
                if knows_secret[p1]:
                    q.add(p1)
                if knows_secret[p2]:
                    q.add(p2)

            q = deque(q)

            while q:
                current_person = q.popleft()
                for next_person in current_meet_map[current_person]:
                    if not knows_secret[next_person]:
                        knows_secret[next_person] = True
                        q.append(next_person)

        return [i for i in range(n) if knows_secret[i]]