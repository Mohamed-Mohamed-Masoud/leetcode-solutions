"""
Intuition:
We can simulate the standard manual mathematical process of multiplying two numbers digit by digit. The key observation is that multiplying a digit at index `i` in `num1` by a digit at index `j` in `num2` affects the result at indices `i + j` (for the carry/tens) and `i + j + 1` (for the ones).

Approach:
1. Create a `result_list` of size `len(num1) + len(num2)` initialized with zeros to hold the intermediate values.
2. Iterate backwards through both strings (from right to left).
3. Extract the integer values of the characters using ASCII values (`ord`).
4. Multiply the two digits and add the product to the current value at `result_list[i + j + 1]`.
5. Update the carry at `result_list[i + j]` and keep only the single digit at `result_list[i + j + 1]`.
6. After the loops, find the first non-zero digit to skip any leading zeros.
7. Convert the remaining elements in the array back to characters and join them into a string. Return "0" if the string is empty.

Complexity:
- Time: O(M * N) - where M and N are the lengths of num1 and num2, respectively, because of the nested loops.
- Space: O(M + N) - to store the intermediate products in the `result_list`.
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result_list = [0] * (len(num1) + len(num2))
        i = len(num1) - 1
        
        while i >= 0:
            j = len(num2) - 1
            while j >= 0:
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                
                ones = i + j + 1
                tens = i + j
                
                result_list[ones] += digit1 * digit2
                
                if result_list[ones] >= 10:
                    result_list[tens] += result_list[ones] // 10
                    result_list[ones] = result_list[ones] % 10
                    
                j -= 1
            i -= 1
            
        first_digit = 0
        while first_digit < len(result_list) and result_list[first_digit] == 0:
            first_digit += 1
            
        result = ""
        for digit in result_list[first_digit:]:
            result += chr(digit + ord('0'))
            
        if not result:
            return "0"
            
        return result