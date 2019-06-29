def binaryGap(self, N: int) -> int:
    a = "{0:b}".format(N)
    res = 0
    for i in range(len(a)):
        if a[i] == '1':
            for j in range(i+1,len(a)):
                if a[j] == '1':
                    res = max(res , j - i)
                    break
    return res