# Intuition
# The problem requires generating all possible letter combinations based on the input digits,
# making the backtracking (recursive) algorithm the intuitive choice to explore all paths and build the strings step by step.

# Approach
# 1. Handle the empty string case as a base condition to return early.
# 2. Use a dictionary to map each digit to its corresponding letters.
# 3. Create a recursive function `calc` that takes the temporary string `letters` as the current path.
# 4. If the length of the current path equals the length of the input digits, append it to the results.
# 5. Otherwise, determine the current digit based on the path length, iterate through its letters, and pass the path appended with the new character to the next recursive call.

# Complexity
# - Time complexity: $O(4^n * n)$
# - Space complexity: $O(n)$

# Code
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        num_dict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9': 'wxyz'}
        result = []
        
        def calc(letters):
            if len(letters) == len(digits):
                result.append(letters)
                return
            else:
                current_digit = digits[len(letters)]
                for char in num_dict[current_digit]:
                    calc(letters + char)
                    
        calc("")
        return result