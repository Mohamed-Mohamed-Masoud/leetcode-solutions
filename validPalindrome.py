# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            elif s[left].isalnum() and not s[right].isalnum():
                right -= 1
            elif not s[left].isalnum() and s[right].isalnum():
                left += 1
            else:
                right -= 1
                left += 1
        return True