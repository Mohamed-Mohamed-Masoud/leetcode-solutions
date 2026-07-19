# Intuition
# The problem is to convert a given string into a zigzag pattern on a given number of rows and then read it line by line.
# The idea is to iterate through each row and collect the characters that belong to that row based on the zigzag pattern.

# Approach
# 1. Initialize an empty list 'result' to store the characters in the zigzag order.
# 2. If the number of rows is 1 or greater than or equal to the length of the string, return the original string as it is.
# 3. Iterate through each row from 0 to `numRows - 1`.
# 4. For each row, initialize an index `i` to the current row number.
# 5. While `i` is less than the length of the string, do the following:
#    a. If the current row is not the last row, append the character at index `i` to the 'result' list and increment `i` by `2 * (numRows - row - 1)`.
#    b. If `i` is still less than the length of the string and the current row is not the first row, append the character at index `i` to the 'result' list and increment `i` by `2 * row`.
# 6. Finally, join the characters in the 'result' list and return the resulting string.

# Complexity
# Time Complexity: O(n), where n is the length of the input string. We are iterating through each character of the string once.
# Space Complexity: O(n), where n is the length of the input string. 

# Code
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = []
        if numRows == 1 or numRows >= len(s):
            return s
        for row in range(numRows):
            i = row
            while i < len(s):
                if row != numRows - 1:
                    result.append(s[i]) 
                    i += 2 * (numRows - row - 1)
                if i < len(s) and row != 0:
                    result.append(s[i]) 
                    i += 2 * row
        return "".join(result)