# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         n=len(nums)
#         left = [0]*n
#         right = [0]*n
        
    
#         for i in range(1,n):
#             left[i] = left[i-1]+ nums[i-1] 

#         for i in range(n-2 , -1 , -1) :
#             right[i] = right[i+1] + nums [i+1]

#         i , j = 0 , 0

#         while(i<n and j<n):
#             if left[i] == right[i] :
#                 return i 
#             i+=1
#             j+=1

#         return -1
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum=0
        for i in nums:
            sum=sum+i
        leftsum=0
        for i in range(len(nums)):
            if i ==0 and sum-nums[i]==0:
                return 0 
            elif i ==len(nums)-1 and leftsum==0:
                return len(nums)-1
            else:
                sum=sum-nums[i]
                if leftsum==sum:
                    return i 
                leftsum=leftsum+nums[i]
        return -1