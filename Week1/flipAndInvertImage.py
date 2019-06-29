def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        A = [[1-j for j in x[::-1]] for x in A]
        return A