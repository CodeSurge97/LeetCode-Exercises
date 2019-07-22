def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        for num in nums1:
            for num1 in nums2[nums2.index(num)::]:
                if num1 > num:  
                    stack.append(num1)
                    break
            else:
                stack.append(-1)
        return stack