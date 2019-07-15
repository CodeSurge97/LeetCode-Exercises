def minDistance(self, word1: str, word2: str) -> int:
        if "" in [word1, word2]: return max(len(word1),len(word2))
        if len(word2)<len(word1): word1,word2=word2,word1
        cur=rec=range(0,len(word1)+1)
        for c in word2:
            rec=cur
            cur=[rec[0]+1]
            for index, e in enumerate(word1):
                if e==c:cur.append(rec[index])
                else:cur.append(min(rec[index+1],rec[index],cur[-1])+1)
        return cur[-1]