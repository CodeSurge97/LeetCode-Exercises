  def sortArrayByParity(self, A: List[int]) -> List[int]:
        list2 = []
        list3 = []
        for num in A:
            if num % 2 == 0:
                list2.append(num)
            else:
                list3.append(num)
        return list2 + list3    