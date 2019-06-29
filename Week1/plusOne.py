def plusOne(self, digits: List[int]) -> List[int]:
        num =''.join(str(e) for e in digits)
        num = int(num) + 1
        result = []
        for x in str(num):
            result.append(int(x))
        return result