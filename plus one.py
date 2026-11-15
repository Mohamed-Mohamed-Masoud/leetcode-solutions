# Intuition:
# Adding one only affects the trailing 9s. A digit that isn't 9 just
# increments and nothing carries further. Each 9 becomes 0 and passes
# a carry to the digit on its left. If every digit is 9 (e.g. 999),
# all of them become 0 and we need a new leading 1 (1000).
#
# Approach:
# 1. Start from the last digit and move left.
# 2. If the current digit isn't 9, increment it and return immediately,
#    since there is no carry left to propagate.
# 3. If it is 9, set it to 0 and continue to the next digit on the left
#    (the carry).
# 4. If the loop finishes, every digit was 9 and is now 0, so prepend
#    a 1 and return [1] + digits.
#
# Complexity:
# Time:  O(n) -- in the worst case (all 9s) we visit every digit once.
# Space: O(1) -- the digits are modified in place. Only the all-9s
#        case builds a new list, which costs O(n).

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        i = len(digits) - 1
        while i >= 0:
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            i -= 1
        return [1] + digits