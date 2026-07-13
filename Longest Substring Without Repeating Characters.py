# Time Complexity : O(N)
# Space Complexity: O(N)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        result = 0
        for char in s:
            while char in seen:
                seen.discard(s[left])
                left += 1
            seen.add(char)
            result = max(len(seen), result)
        return result