class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        '''
        i = 0 
        j = 0 
        ans = []
        while i < len(nums1) and j < len(nums2) :
            if nums1[i][0] == nums2[j][0] :
                ans.append([nums1[i][0],nums1[i][1] + nums2[i][1] ])
                i+=1 
                j+=1 
            elif nums1[i][0]<nums2[i][0] :
                ans.append( [nums1[i][0] , nums1[i][1] ] ) 
                i+=1 
            else :
                ans.append( [nums2[i][0] , nums2[i][1]]) 

        return ans        
        '''

        dic = {} 
        for i in nums1 :
            dic[i[0]] = i[1] 
        for j in nums2 :
            if j[0] in dic :
                dic[j[0]] += j[1] 
            else :
                dic[j[0]] = j[1] 

        return sorted(list(dic.items()))
