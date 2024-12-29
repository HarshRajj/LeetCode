class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        ans = []
        if len(strs)==0:
            return [[""]]

        for i in range(len(strs)):
            k=''.join(sorted(strs[i]))
            

            if k in dic:
                dic[k].append(strs[i])
                                   


            else:

                dic[k] =[strs[i]]
        for value in dic.values():
            ans.append(value)
        return ans 
                         