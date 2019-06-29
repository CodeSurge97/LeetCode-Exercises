def fizzBuzz(self, n: int) -> List[str]:
        result = []
        num = ""
        for x in range(1,n+1):
            if x % 3 == 0 and x % 5 == 0:
                num = "FizzBuzz"
            elif x % 3 == 0:
                num = "Fizz"
            elif x % 5 == 0:
                num = "Buzz"
            else:
                num = str(x)
            result.append(num)
        return result