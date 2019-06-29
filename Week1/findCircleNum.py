 def findCircleNum(self, M: List[List[int]]) -> int:
    N=len(M)
    visited,count=set(),0
    def dfs(node):
        for j in range(N):
            if M[node][j]==1 and j not in visited:
                visited.add(j)
                dfs(j)
    for i in range(N):
        if i not in visited:
            count+=1
            dfs(i)
    return count