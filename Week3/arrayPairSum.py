def arrayPairSum(self, nums: List[int]) -> int:
        lnums = sorted(nums)
        result = 0
        for i,k in zip(lnums[0::2], lnums[1::2]):
            result += min(i,k)
        return result