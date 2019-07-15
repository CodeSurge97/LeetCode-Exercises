def lemonadeChange(self, bills: List[int]) -> bool:
        change = []
        result = True
        for i in bills:
            if i == 5:
                change.append(i)
            elif i == 10:
                if 5 not in change:
                    result = False
                else:
                    change.append(i)
                    change.remove(5)
            else:
                if 10 not in change: 
                    if change.count(5) < 3:
                        result = False
                    else:
                        change.append(20)
                        change.remove(5)
                        change.remove(5)
                        change.remove(5)
                elif 5 not in change:
                    result = False
                else:
                    change.append(i)
                    change.remove(10)
                    change.remove(5)
        return result