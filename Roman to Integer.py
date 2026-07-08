# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def romanToInt(self, s: str) -> int:
        num_list = []
        for letter in s:
            if letter == 'I':
                num_list.append(1)
            elif letter == 'V':
                num_list.append(5)
            elif letter == 'X':
                num_list.append(10)
            elif letter == 'L':
                num_list.append(50)
            elif letter == 'C':
                num_list.append(100)
            elif letter == 'D':
                num_list.append(500)
            elif letter == 'M':
                num_list.append(1000)
            else:
                raise ValueError("Symbol not vaild")
        result = 0
        i = 0
        while i < len(num_list) - 1:
            if num_list[i] < num_list[i+1]:
                result += num_list[i+1] - num_list[i]
                i += 2
            else:
                result += num_list[i]
                i += 1
        if i == len(num_list) - 1:
            result += num_list[i]
        return result

        