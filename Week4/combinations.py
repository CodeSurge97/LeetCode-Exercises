def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        nums = [i for i in range(1, n+1)]
        
        if k == 1: return [[i] for i in nums]
        
        def dfs(cache, index):
            
            if len(cache) == k:
                result.append(cache.copy())
                return
            
            if index == len(nums):
                return
            
            for i in nums[index:]:
                cache.append(i)
                dfs(cache, index+1)
                cache.pop()
                index += 1

        for index, i in enumerate(nums[:-k+1]): dfs([i], index+1)
        
        return result