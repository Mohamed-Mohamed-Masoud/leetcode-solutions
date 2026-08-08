"""
Intuition
Anagrams share the exact same frequency of characters. Instead of sorting each string to find a common key, 
we can generate a character count array of size 26 for each word. 
This count array can act as a unique signature (key) in a Hash Table to group all matching anagrams together.

Approach
1. Initialize a hash dictionary `str_dict` to store the grouped anagrams.
2. Iterate through each `word` in the given list of strings `strs`.
3. For each `word`, create a `count` list of 26 zeros to represent the alphabet.
4. Iterate through each character `c` in the `word`, calculating its alphabetical index using `ord(c) - ord('a')`, and increment the respective counter.
5. Convert the `count` list into a tuple so it can be used as an immutable, hashable key in the dictionary.
6. Append the original `word` to the dictionary using the tuple as the key.
7. Return all grouped anagram lists by extracting `str_dict.values()`.

Complexity
- Time complexity: O(N * K) where N is the number of strings and K is the maximum length of a string. We traverse each character of each string exactly once.
- Space complexity: O(N * K) to store the grouped strings within the Hash Table.
"""

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c)-ord('a')] += 1
            
            count = tuple(count)
            
            if count in str_dict:
                str_dict[count].append(word)
            else:
                str_dict[count] = [word]
                
        return list(str_dict.values())