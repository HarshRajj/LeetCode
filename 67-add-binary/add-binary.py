class Solution:
    
    def trim(self, s)-> str :
        firstOne = s.find('1') 
        return s[firstOne : ] if firstOne != -1 else "0"
    
    def addBinary(self, a: str, b: str) -> str:
		# code here
        s1 = self.trim(a)
        s2 = self.trim(b) 

        n= len(s1)
        m = len(s2) 
        
        if n < m :
            s1, s2  = s2, s1
            n, m = m, n 
            
        result = []
        bit1, bit2 = 0, 0 
        carry = 0
        j = m-1
            
        for i in range(n-1, -1, -1) :
            
            bit1 = int(s1[i])
            bitSum = bit1 + carry
            
            if j >= 0 :
                bit2 = int(s2[j])
                bitSum = bitSum + bit2 
                j-=1
                
                
            bit = bitSum%2 
            carry = bitSum//2
            
            result.append(str(bit))
            
        if carry == 1 :
            result.append("1") 
            
        return ''.join(result[::-1])
        