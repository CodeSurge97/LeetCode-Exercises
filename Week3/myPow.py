def myPow(self, x: float, n: int) -> float:
        # First Version. Time complexity O(logn). Space comlexity O(1)
	    if n >= 0:
		    return self.getPow(x, n)
	    else:
		    return 1 / self.getPow(x, -n)


def getPow(self, x, m):
	if m == 0:
		return 1
	else:
		if m % 2 == 0:
			return self.getPow(x * x, m // 2)
		elif m % 2 == 1:
			return x * self.getPow(x * x, m // 2)