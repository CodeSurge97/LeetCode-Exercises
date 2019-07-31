def exist(self, board: List[List[str]], word: str) -> bool:
        queue = []
        M = len(board)
        N = len(board[0])
        
        def dfs(i,j,b,index):
            if index == len(word):
                return True
            if i < 0 or j < 0 or i == M or j == N:
                return False
            if b[i][j] != word[index]:
                return False
            tmp = b[i][j]
            b[i][j] = '0'
            ans = dfs(i-1,j,b,index+1) or dfs(i+1,j,b,index+1) or dfs(i,j-1,b,index+1)                         or dfs(i,j+1,b,index+1) 
            b[i][j] = tmp
            return ans
        
        for i in range(M):
            for j in range(N):
                if dfs(i,j,board,0):
                    return True