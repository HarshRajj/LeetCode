class ProductOfNumbers:

    def __init__(self):
        self.ls = []
    
    def add(self, num: int) -> None:
        if num == 0:
            self.ls.clear() 
        else:
            if self.ls:
                self.ls.append(self.ls[-1] * num) 
            else:
                self.ls.append(num) 
    
    def getProduct(self, k: int) -> int:
        if k > len(self.ls):  
            return 0 
        if k == len(self.ls):
            return self.ls[-1]
        
        return self.ls[-1] // self.ls[-k-1]