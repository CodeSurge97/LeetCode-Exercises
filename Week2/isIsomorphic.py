def isIsomorphic(self, s: str, t: str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping = {}
        set_ = set()
        for i in range(len(s)):
            
            if s[i] not in mapping and t[i] in set_:
                return False
            
            elif s[i] not in mapping:
                mapping[s[i]] = t[i]
                set_.add(t[i])
                
            elif mapping[s[i]] != t[i]:
                return False
            

        return True
