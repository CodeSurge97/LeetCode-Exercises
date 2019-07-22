def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        perms = []
        for pi in self.permute(nums[1:]):
            for i in range(len(nums)):
                perms.append(pi[:i] + [nums[0]] + pi[i:])
        return perms