"""
Intuition:
Navigating a hierarchical file system naturally follows a Last-In-First-Out (LIFO) pattern. A stack is the perfect data structure for this problem, allowing us to easily keep track of valid directories and backtrack when we encounter a parent directory command ("..").

Approach:
1. Split the input path by the '/' delimiter to break it down into manageable components (directories and commands).
2. Initialize an empty stack (using a list) to build the valid simplified path.
3. Iterate through the parsed components:
   - If the component is empty (due to multiple slashes) or a single dot ('.'), ignore it and continue.
   - If the component is a double dot ('..'), pop the last directory from the stack if it's not empty (moving one level up).
   - Otherwise, append the valid directory name to the stack.
4. Finally, construct the canonical path by joining the stack elements with '/' and prepending a leading '/'.

Complexity:
- Time: O(N) - where N is the length of the input path. Splitting the string and processing each component takes linear time.
- Space: O(N) - to store the split array and the stack, which in the worst case could hold all the directories.
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        directory_list = path.split('/')
        result = []
        
        for directory in directory_list:
            if directory in ['', '.']:
                continue
            elif directory == '..':
                if result:
                    result.pop()
                continue
            
            result.append(directory)
            
        return '/' + '/'.join(result)