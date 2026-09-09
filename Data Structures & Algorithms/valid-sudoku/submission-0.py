class Solution:
    def isValidMove(board, row, col, num):
        box_idx = (row // 3, col // 3 )

        if num in rows[row] or num in cols[col] or num in boxes[box_idx]:
            return False

    def place_number(row, col, num):
        box_idx = (row // 3, col // 3)

        rows[row].add(num)
        cols[col].add(num)
        boxes[box_idx].add(num)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i: set() for i in range(9)}
        cols = {i: set() for i in range(9)}
        boxes = {(r,c): set() for r in range(3) for c in range(3)}

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                
                box_idx = (r // 3, c // 3)

                if num in rows[r] or num in cols[c] or num in boxes[box_idx]:
                    return False
                
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_idx].add(num)

        return True