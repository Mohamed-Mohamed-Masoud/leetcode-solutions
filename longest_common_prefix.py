# Time Complexity: O(N log N * M) - where N is the number of strings and M is the maximum string length due to sorting.
# Space Complexity: O(1) or O(M) - auxiliary space for the result string.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        result = ""
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                result += strs[0][i]
            else:
                break
        return result