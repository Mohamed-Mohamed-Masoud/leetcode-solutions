# Intuition:
# Every row of Pascal's Triangle depends only on the row right before
# it, so there is no need to store the whole triangle. We keep just the
# previous row and use it to build the next one, until we reach the
# row at index rowIndex.
#
# Approach:
# 1. Start with an empty list result that holds the previous row.
# 2. For each row from 0 to rowIndex, build a new list row_list with
#    row + 1 elements.
# 3. For each position i in the row:
#    - If i is the first (0) or last (row) position, append 1.
#    - Otherwise, append result[i-1] + result[i], the two neighbors
#      above it in the previous row.
# 4. Replace result with a copy of row_list, so it becomes the
#    "previous row" for the next iteration.
# 5. After the loop, result holds row number rowIndex, so return it.
#
# Complexity:
# Time:  O(rowIndex^2) -- row k costs k + 1 steps, so the total is
#        1 + 2 + ... + (rowIndex + 1), which is about rowIndex^2 / 2.
# Space: O(rowIndex) -- only the previous row and the current row are
#        kept, each with at most rowIndex + 1 elements.

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        result = []
        for row in range(rowIndex + 1):
            row_list = []
            for i in range(row + 1):
                if i == 0 or i == row:
                    row_list.append(1)
                else:
                    calc = result[i] + result[i - 1]
                    row_list.append(calc)
            result = row_list[:]
        return result