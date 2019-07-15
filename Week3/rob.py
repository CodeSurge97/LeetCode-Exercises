def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n <= 2: return max(nums)
        DP0 = [0] * n;
        DP1 = [0] * n;

        DP0[-1] = nums[-1]
        DP0[-2] = max(nums[-1],nums[-2])

        DP1[-1] = 0
        DP1[-2] = nums[-2]

        for i in range(n-3,0,-1):
            DP0[i] = max(nums[i] + DP0[i+2],DP0[i+1])
            DP1[i] = max(nums[i] + DP1[i+2],DP1[i+1])
        return max(nums[0] + DP1[2],DP0[1])