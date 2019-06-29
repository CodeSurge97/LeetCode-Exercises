def findComplement(self, num: int) -> int:
        bnum = bin(num)
        intList = [1-int(j) for j in bnum[2::]]
        result = 0
        for bit in intList:
            result = (result << 1) | bit
        return result