def isPalindrome(self, s: str) -> bool:
        s = s.casefold()
        revS = s[::-1]
        return [c for c in s if c.isalnum()] == [c for c in revS if c.isalnum()]