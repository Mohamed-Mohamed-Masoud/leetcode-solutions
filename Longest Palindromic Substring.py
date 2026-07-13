# Time Complexity : O(N * N)
# Space Complexity: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return s
        result = ""
        def checkPalindrome(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        for i in range(len(s)):
            result = max(result, checkPalindrome(i,i), checkPalindrome(i,i+1), key=len)
        return result