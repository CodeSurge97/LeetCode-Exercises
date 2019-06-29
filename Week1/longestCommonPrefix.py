def longestCommonPrefix(self, strs: List[str]) -> str:
        result =""
        if not strs:
            return result 
        m, n = len(strs), len(strs[0])
        for i in range(n):
            for j in range(m):
                if(i>=len(strs[j]) or strs[j][i]!=strs[0][i]):
                    return result
            result+=strs[0][i]
        return resul