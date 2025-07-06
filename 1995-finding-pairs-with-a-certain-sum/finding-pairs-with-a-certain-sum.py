class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        
        self.nums1 = nums1 
        self.nums2= nums2
        self.dic = Counter(nums2)

        

    def add(self, index: int, val: int) -> None:

        p = self.nums2[index]
        self.dic[p] -= 1
        if self.dic[p] <= 0 :
            self.dic.pop(p)

        self.nums2[index] += val 
        self.dic[self.nums2[index]] += 1
        
    def count(self, tot: int) -> int:
        count = 0 
        for val in self.nums1 :
            count+= self.dic[tot - val]

        return count
        

        


        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)