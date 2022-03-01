class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n  = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        wordLen = len(word)
        
        def isExist(x, y):
            if x >= 0 and y >= 0 and x < m and y < n:
                return True
            return False
        
        def dfs(row, col, pos):
            temp = board[row][col]
            
            if pos == wordLen:
                return True
            board[row][col] = "#"
            for x, y in directions:
                dx, dy = row + x, col + y
                if isExist(dx, dy) and board[dx][dy] == word[pos]:
                    if dfs(dx, dy, pos + 1):
                        return True
            board[row][col] = temp
            
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1):
                        return True
        return False
