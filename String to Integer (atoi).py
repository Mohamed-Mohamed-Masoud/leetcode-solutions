# Intuition
# The problem is to convert a string to an integer (atoi) following specific rules, such as ignoring leading whitespace,
#   handling optional signs, and stopping at the first non-digit character.

# Approach
# 1. Initialize a boolean variable 'first' to track if we are still processing the leading characters.
# 2. Initialize an index 'i' to 0 to iterate through the string.
# 3. While 'i' is less than the length of the string, do the following:
#    a. If the current character is a digit or a sign ('+' or '-') and we are still processing leading characters, set 'first' to False and increment 'i'.
#    b. If the current character is a space and we are still processing leading characters, increment 'i'.
#    c. If neither condition is met, break the loop as we have reached the end of the leading characters.
# 4. Try to convert the substring from the start of the string to index 'i' into an integer. If it raises a ValueError, set the result to 0.
# 5. Check if the result is within the 32-bit signed integer range. If it exceeds the maximum, return 2**31 - 1. If it is below the minimum, return -2**31. Otherwise, return the result.

# Complexity
# Time Complexity: O(n), where n is the length of the input string. We are iterating through each character of the string once.
# Space Complexity: O(1), as we are using a constant amount of space for variables

# Code
class Solution:
    def myAtoi(self, s: str) -> int:
        first = True
        i = 0
        
        while i < len(s):
            if s[i].isdigit() or s[i] in '+-' and first:
                first = False
                i += 1
            elif s[i] == ' ' and first:
                i += 1
            else:
                break

        try:
            result = int(s[:i])
        except ValueError:
            result = 0
        
        if result > 2**31 - 1:
            return 2**31 - 1
        elif result < -2**31:
            return -2**31
        else:
            return result