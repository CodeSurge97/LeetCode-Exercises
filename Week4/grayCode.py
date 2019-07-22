def grayCode(self, n: int) -> List[int]:
        ans = [0]
        for i in range(n):
            # i increases to i+1
            # the length of the answer increases from 2**i to 2*(i+1)
            # the new 2**i elements are 2**i larger than the old elements
            # and reversed order
            ans = ans + [j+2**i for j in ans][::-1]
        return ans