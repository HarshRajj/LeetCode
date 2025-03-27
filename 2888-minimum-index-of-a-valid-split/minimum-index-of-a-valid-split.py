class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dic = Counter(nums) 
        dominant = 0 
        n = len(nums) 

        for key, val in dic.items() :
            if val > n /2 :
                dominant = key
                break 

        f1 = 0 
        for i, num in enumerate (nums) :
            if num == dominant :
                f1 += 1 

            if (i + 1) // 2 < f1 and (n-i-1)//2 < dic[dominant]-f1 :
                return i 

        return -1
        
        