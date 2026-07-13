# Time Complexity : O(N * M)
# Space Complexity: O(1)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)