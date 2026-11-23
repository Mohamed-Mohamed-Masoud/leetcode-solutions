# Intuition:
# Two strings are anagrams if they contain exactly the same characters
# with the same frequencies. Instead of building two separate counts and
# comparing them, we use one hash table: add 1 for each character of s
# and subtract 1 for each character of t. If they are anagrams, every
# count ends at 0.
#
# Approach:
# 1. If the lengths differ, return False immediately, since they
#    can't be anagrams.
# 2. Create an empty hash table (dict) called counter.
# 3. Loop over the indices i of both strings at the same time:
#    - Increment counter[s[i]] by 1.
#    - Decrement counter[t[i]] by 1.
# 4. After the loop, check that every value in counter is 0. If so,
#    both strings have identical character frequencies, so return True.
#    Otherwise return False.
#
# Complexity:
# Time:  O(n) -- one pass over the strings, plus a pass over the
#        counter values (at most k distinct characters, k <= n).
# Space: O(k) -- where k is the number of distinct characters. It is
#        O(1) if the alphabet is fixed (e.g. 26 lowercase letters).

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t or len(s) != len(t):
            return False
        counter = {}
        for i in range(len(s)):
            counter[s[i]] = counter.get(s[i], 0) + 1
            counter[t[i]] = counter.get(t[i], 0) - 1
        return all(value == 0 for value in counter.values())