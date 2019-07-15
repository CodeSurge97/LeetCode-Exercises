def peakIndexInMountainArray(self, A: List[int]) -> int:
    for i, c in enumerate(A):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            return i