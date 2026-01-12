class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0 
        for i in range(len(points)-1) :
            hor = abs(points[i][0]- points[i+1][0])
            ver = abs(points[i][1]- points[i+1][1])
            ans += max(hor, ver)

        return ans


        