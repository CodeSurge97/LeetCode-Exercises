def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        s = [x[::-1] for x in words]
        s = " ".join(s) 
        return s