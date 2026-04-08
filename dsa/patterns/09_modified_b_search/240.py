class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        r, c = len(matrix)-1, 0
        while r>=0 and c<len(matrix[0]):
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                c += 1
            else:
                r -= 1
        return False

if __name__ == '__main__':
    o = Solution()
    print(o.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))
    print(o.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))
    print(o.searchMatrix([[3,3,8,13,13,18],[4,5,11,13,18,20],[9,9,14,15,23,23],[13,18,22,22,25,27],[18,22,23,28,30,33],[21,25,28,30,35,35],[24,25,33,36,37,40]], 21))
