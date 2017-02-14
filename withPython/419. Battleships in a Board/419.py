class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        row = len(board)
        column= len(board[0])
        cnt=0
        notsearch=[[True for j in range(column)] for i in range(row)]
        for i in range(row):
            for j in range(column):
                if notsearch[i][j] and board[i][j] == 'X':
                    notsearch[i][j] = False
                    cnt+=1
                    self.down(board, notsearch, i, j)
                    self.right(board, notsearch, i, j)
        return cnt            
    def down(self, board, notsearch, i, j):
        if i+1 < len(board) and board[i+1][j] == 'X':
            notsearch[i+1][j] = False
            self.down(board, notsearch, i+1, j)
    def right(self, board, notsearch, i, j):
        if j+1 < len(board[0]) and board[i][j+1] == 'X':
            notsearch[i][j+1] = False
            self.right(board, notsearch, i, j+1)