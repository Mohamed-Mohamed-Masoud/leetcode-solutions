# Intuition
# We can solve this using a greedy approach. 
# By always subtracting the largest possible Roman number value from the number,
# we can build the string efficiently until the number reaches zero.


# Approach

# 1. Create a list of tuples, roman_map, storing the integers and their Roman string equivalents in descending order.
# 2. Iterate through roman_map. For each key (value), use divmod(num, key) to find out how many times the val (symbol) should be added.
# 3. Update num to be the remainder.
# 4. Stop the loop early if num becomes 0.
# 5. Append the symbols to a list and use "".join() at the end for optimal string concatenation.


# Complexity

# Time complexity: O(1) 
# the time taken is independent of the input size.

# Space complexity: O(1)
# The memory used by roman_map is constant, and the output string length has limit.


# Code
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_map = [(1000,'M'), (900,'CM'), (500,'D'), (400,'CD'), (100,'C'), (90,'XC'), (50,'L'),
                     (40,'XL'), (10,'X'), (9,'IX'), (5,'V'), (4,'IV'), (1,'I')]
        result = []

        for key, val in roman_map:
            if num == 0:
                break
            count, num = divmod(num, key)
            result.append(val * count)
        
        return "".join(result)