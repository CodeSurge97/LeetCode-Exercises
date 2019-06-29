def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        
        def neighbors(x, y)->List[List[int]]:
            ans = []
            if x + 1 < m and board[x + 1][y] == 'O':
                ans.append([x + 1, y])
            if x - 1 >= 0 and board[x - 1][y] == 'O':
                ans.append([x - 1, y])
            if y + 1 < n and board[x][y + 1] == 'O':
                ans.append([x, y + 1])
            if y - 1 >= 0 and board[x][y - 1] == 'O':
                ans.append([x, y - 1])
            return ans
            
        def dfs(i:int, j:int)->None: #mark O as S then changed it back to O
            board[i][j] = 'S'
            for neighbor in neighbors(i,j):
                x, y = neighbor
                dfs(x, y)
            return
        
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n - 1] == 'O':
                dfs(i, n - 1)
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[m - 1][j] == 'O':
                dfs(m - 1, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'S':
                    board[i][j] = 'O'
        
        return