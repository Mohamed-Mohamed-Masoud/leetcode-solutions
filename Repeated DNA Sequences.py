# Intuition:
# I used set to find the correct sequences without duplicaties and high speed

# Approach:
# 1. Create a set to store seen sequences and a set to store the result.
# 2. Iterate through the string, extracting each 10-letter-long sequence.
# 3. If the sequence is already in the seen set, add it to the result set.

# Complexity:
# Time complexity: O(N), where N is the length of the string.
# Space complexity: O(N), where N is the number of unique sequences.


# Code
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        result = set()
        for i in range(len(s)-9):
            DNA = s[i:i+10]
            if DNA in seen:
                result.add(DNA)
            else:
                seen.add(DNA)
        return list(result)
        