# Original Approach
# Time Complexity: O(N)
# Space Complexity: O(1) - Bounded by the fixed ASCII character set size.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st_set = set(zip(s,t))
        return len(st_set) == len(set(s)) and len(st_set) == len(set(t))