class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        def recur(r):
            if r == n:
                outp.append([''.join(a) for a in curr])
                return
            for c in range(n):
                if r in rows or c in cols or r+c in fdia or r-c in bdia:
                    continue
                rows.add(r)
                cols.add(c)
                fdia.add(r+c)
                bdia.add(r-c)
                curr[r][c] = 'Q'
                recur(r+1)
                curr[r][c] = '.'
                rows.remove(r)
                cols.remove(c)
                fdia.remove(r+c)
                bdia.remove(r-c)
        curr = [['.'] * n for _ in range(n)]
        outp = []
        rows, cols, fdia, bdia = set(), set(), set(), set()
        recur(0)
        return outp

if __name__ == '__main__':
    o = Solution()
    print(o.solveNQueens(4))
    print(o.solveNQueens(1))
