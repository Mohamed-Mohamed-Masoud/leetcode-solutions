class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            s = str(x)
            l = len(s)
            for i in range(l//2):
                if s[i] != s[l-i-1]:
                    return False
            return True
            