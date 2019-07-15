def isSubsequence(self, s: str, t: str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i,j = len(s) - 1,len(t) - 1
        while i >= 0 and j >= 0:
            if s[i] == t[j]:
                i -= 1
                j -= 1
            else:
                j -= 1
        
        return i < 0