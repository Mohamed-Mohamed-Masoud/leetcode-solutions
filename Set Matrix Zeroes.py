"""
Intuition
If we modify the matrix in-place while iterating, we might incorrectly propagate zeros to other rows and columns. To prevent this, we can first locate and save the exact coordinates of all the original zeros. Once we have the locations, we can use them to update the respective rows and columns safely in a second pass.

Approach
1. Initialize an empty list `zeros` to keep track of the original zero coordinates.
2. Traverse every element in the `matrix` using nested loops for rows and columns.
3. When a `0` is encountered, append its coordinate `(r, c)` to the `zeros` list.
4. After finding all original zeros, iterate through the stored `zeros` list.
5. For each `(r, c)` coordinate, overwrite the entire row `r` with a list of zeros.
6. Then, iterate through all rows `i` to set `matrix[i][c] = 0`, successfully zeroing out the entire column `c`.

Complexity
- Time complexity: O(M * N + Z * (M + N)) where M is the number of rows, N is the number of columns, and Z is the total number of zeros found. We traverse the matrix once, then for each zero, we update its row and column.
- Space complexity: O(Z) to store the coordinates of the zeros, which in the worst case scales up to O(M * N) if the matrix is entirely filled with zeros.
"""

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeros = []
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    zeros.append((r, c))
                    
        for r, c in zeros:
            matrix[r] = [0] * len(matrix[r])
            for i in range(len(matrix)):
                matrix[i][c] = 0