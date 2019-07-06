def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        if len(p) > len(s): return result
        d1, d2 = [0] * 26, [0] * 26
        for i in range(len(p)):
            d1[ord(s[i]) - 97] += 1
            d2[ord(p[i]) - 97] += 1
        if d1 == d2: result.append(0)
        for i in range(1, len(s) - len(p) + 1):
            d1[ord(s[i + len(p) - 1]) - 97] += 1
            d1[ord(s[i - 1]) - 97] -= 1
            if d1 == d2: result.append(i)
        return result