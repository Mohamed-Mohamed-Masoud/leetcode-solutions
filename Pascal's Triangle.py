# Intuition:
# In Pascal's Triangle, every row starts and ends with 1, and each
# inner value is the sum of the two values directly above it in the
# previous row. So each row can be built entirely from the row before it.
#
# Approach:
# 1. Create an empty list result to hold all rows.
# 2. For each row index from 0 to numRows - 1, start a new empty row.
#    Row number `row` contains row + 1 elements.
# 3. For each position i in the row:
#    - If i is the first (0) or last (row) position, append 1.
#    - Otherwise, append result[row-1][i-1] + result[row-1][i], the
#      two neighbors above it.
# 4. After all rows are built, return result.
#
# Complexity:
# Time:  O(numRows^2) -- row k has k + 1 elements, so the total number
#        of elements is 1 + 2 + ... + numRows, which is about numRows^2 / 2.
# Space: O(numRows^2) -- the output triangle stores all those elements.
#        Extra space beyond the output is O(1).

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = []
        for row in range(numRows):
            result.append([])
            for i in range(row + 1):
                if i == 0 or i == row:
                    result[row].append(1)
                else:
                    calc = result[row - 1][i] + result[row - 1][i - 1]
                    result[row].append(calc)
        return result