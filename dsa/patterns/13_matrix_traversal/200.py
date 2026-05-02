class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def recur(r, c):
            if r in range(len(grid)) and c in range(len(grid[0])) and grid[r][c] == '1':
                grid[r][c] = ilnd
                recur(r-1, c)
                recur(r+1, c)
                recur(r, c-1)
                recur(r, c+1)
        ilnd = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    recur(r, c)
                    ilnd += 1
        return ilnd

if __name__ == '__main__':
    o = Solution()
    print(o.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
    print(o.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
