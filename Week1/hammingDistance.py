def hammingDistance(self, x: int, y: int) -> int:
        x,y = format(x, '032b'),format(y,'032b')
        result = 0
        for xbit, ybit in zip(x,y):
            if xbit != ybit:
                    result += 1
        return result