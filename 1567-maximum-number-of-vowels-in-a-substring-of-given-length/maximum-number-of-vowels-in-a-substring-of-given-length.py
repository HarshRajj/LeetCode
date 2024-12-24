class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0 
        r = k-1 
        cnt = 0
        vow = "aeiou"
        # while(r<len(s)):
        #     for i in range(l,r+1) :
        #         if s[i] in vow :
        #             cnt +=1 
        #     maxcnt = max(cnt, maxcnt)
        #     cnt = 0
        #     l+=1
        #     r+=1
        # return maxcnt

        for i in range(0,k) :
            if s[i] in vow :
                cnt +=1
        maxcnt = cnt 

        for i in range(k,len(s)):
            if s[i] in vow :
                cnt += 1
            if s[i-k] in vow :
                cnt -= 1 
            maxcnt = max(cnt, maxcnt)

        return maxcnt

        
