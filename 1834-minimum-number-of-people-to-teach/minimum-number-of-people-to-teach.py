class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:

        langs = [set(l) for l in languages]
        bad_users = set()
        for u, v in friendships:
            u -= 1
            v -= 1
            if langs[u].isdisjoint(langs[v]):
                bad_users.add(u)
                bad_users.add(v)

        if not bad_users:
            return 0

        min_teach = float('inf')
        for lang in range(1, n + 1):
            need_teach = sum(1 for u in bad_users if lang not in langs[u])
            min_teach = min(min_teach, need_teach)

        return min_teach

        