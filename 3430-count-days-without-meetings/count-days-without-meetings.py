class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        merged = []
        for meet in meetings :
            if not merged or meet [0] > merged [-1][1] :
                merged.append(meet) 
            else :
                merged[-1][1] = max(merged[-1][1] , meet[1])

        meet_days = 0 
        for i, j in merged :
            meet_days += j - i + 1

        return days- meet_days
        