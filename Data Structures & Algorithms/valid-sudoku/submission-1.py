class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if (board[row][col] == "."):
                    continue

                if (board[row][col] in rows[row] or board[row][col] in columns[col] or board[row][col] in squares[(row//3, col//3)]):
                    return False

                columns[col].add(board[row][col])
                rows[row].add(board[row][col])
                squares[(row//3, col//3)].add(board[row][col])
        return True

# Time complexity : o(n^2)
# space complexity : o(n^2)
        