class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int] :
        n = len(nums) 
        st = set()
        for j in range(n) :
            if nums[j] == key :
                start = max(0, j-k) 
                end = min(n-1, j+k)
                for ind in range(start, end+1) :
                    st.add(ind)

        return list(st)


        