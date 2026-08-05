"""
Intuition
To validate the Sudoku board, we must ensure there are no duplicate numbers in any row, column, or 3x3 sub-box. 
Hash Tables (sets) combined with Arrays provide an efficient way to keep track of the seen digits with constant time lookups.

Approach
1. Initialize arrays of Hash Sets to track the seen digits for each of the 9 rows, 9 columns, and 9 sub-boxes.
2. Iterate through each cell in the 9x9 grid.
3. Skip the cell if it is empty ('.').
4. Calculate the corresponding box index using `row_i // 3 + column_i // 3 * 3`.
5. Check if the current digit already exists in its respective row set, column set, or box set. If it does, return `False`.
6. Otherwise, add the digit to the respective sets and continue.
7. If the loop completes without finding any duplicates, return `True`.

Complexity
- Time complexity: O(1) or O(9^2) because the board size is fixed at 9x9, requiring exactly 81 operations.
- Space complexity: O(1) or O(9^2) because the sets will store at most 81 elements in total, which is a constant space.
"""

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        empty = '.'
        row = [set() for _ in range(9)]
        column = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        
        for row_i in range(9):
            for column_i in range(9):
                digit = board[row_i][column_i]
                if digit == empty:
                    continue
                
                if digit in row[row_i] or digit in column[column_i] or digit in box[row_i // 3 + column_i // 3 * 3]:
                    return False
                    
                row[row_i].add(digit)
                column[column_i].add(digit)
                box[row_i // 3 + column_i // 3 * 3].add(digit)
                
        return True