def isHappy(self, n: int) -> bool:
        num = str(n)
        unique = []
        ans = True
        loop = True
        
        while loop:
            s = 0
            for i in num:
                s = s + (int(i))**2
                
            num = str(s)
            
            if s == 1:
                loop = False
            elif s not in unique:
                unique.append(s)
            else:
                ans = False
                loop = False
        
        return ans