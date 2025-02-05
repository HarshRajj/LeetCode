class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        un = []
        for i in range(len(s1)):
            if s1[i]!= s2[i]:
                un.append([s1[i], s2[i]])
                if len(un)>2 :
                    return False 

        if not un :
            return True 

        return len(un)==2 and un[0] == un[1][::-1]

            

                

        



        

