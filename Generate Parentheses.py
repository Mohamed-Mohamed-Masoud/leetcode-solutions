"""
Intuition:
To generate all valid parentheses combinations, we can build the strings character by character. 
A combination is valid if we never close a parenthesis before opening one, and we use exactly 'n' open and 'n' close parentheses.

Approach:
We use a Backtracking approach to explore all valid paths:
1. Track the count of open (n_open) and close (n_close) parentheses.
2. Base case: If the sum of open and close parentheses equals 2 * n, a valid combination is formed and added to the result.
3. Recursive step 1: If n_open < n, we can safely add an open parenthesis '('.
4. Recursive step 2: If n_close < n_open, we can safely add a close parenthesis ')'.

Complexity:
- Time Complexity: O(4^n / sqrt(n)), which represents the nth Catalan number. We only generate valid combinations without wasting time on invalid ones.
- Space Complexity: O(n) for the recursion call stack, as the maximum depth of the recursion tree will be 2 * n.
"""
# Code
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def generate(combination, n_open, n_close):
            if n_open + n_close == 2 * n:
                result.append(combination)
                return
            if n_open < n:
                generate(combination+'(', n_open+1, n_close)
            if n_close < n_open:
                generate(combination+')', n_open, n_close+1)
        generate("", 0, 0)
        return result