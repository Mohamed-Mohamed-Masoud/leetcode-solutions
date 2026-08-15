"""
Intuition:
The problem requires us to generate the nth term of a sequence by reading aloud the (n-1)th term (run-length encoding). We can naturally solve this using recursion by fetching the previous sequence and then counting consecutive identical characters to build the current one.

Approach:
1. Base case: If n == 1, return the string "1".
2. Recursively call the function for n - 1 to get the previous sequence (`prev_seq`).
3. Iterate through `prev_seq`, keeping track of the current character (`ref`) and its `count`.
4. If the current character matches `ref`, increment the `count`.
5. If it differs, append the `count` and `ref` to the `result` string, update `ref` to the new character, and reset `count` to 1.
6. After the loop, append the final group's count and character to the result and return it.

Complexity:
- Time: O(2^n) - The length of the sequence grows exponentially with each step, and we iterate through the entire string at each level of recursion.
- Space: O(n) - The recursion stack will go up to depth n. Additionally, space is used to store intermediate strings.
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        prev_seq = self.countAndSay(n-1)
        result = ""
        ref = prev_seq[0]
        count = 0
        
        for num in prev_seq:
            if num != ref:
                result += str(count) + ref
                ref = num
                count = 1
            else:
                count += 1
                
        result += str(count) + ref
        
        return result