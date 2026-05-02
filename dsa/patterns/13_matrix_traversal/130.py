class Solution:
    def solve(self, board: list[list[str]]) -> None:
        outr = set()
        def recur(r, c):
            if r in range(len(board)) and c in range(len(board[0])) and board[r][c] == 'O':
                board[r][c] = ilnd
                if r == 0 or c == 0 or r == len(board)-1 or c == len(board[0])-1:
                    outr.add(ilnd)
                recur(r-1, c)
                recur(r, c-1)
                recur(r+1, c)
                recur(r, c+1)
        ilnd = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    recur(r, c)
                    ilnd += 1
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in outr:
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'
        return board

if __name__ == '__main__':
    o = Solution()
    print(o.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
    print(o.solve([["X"]]))
