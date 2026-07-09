# Original Approach
# Time Complexity: O(logN)
# Space Complexity: O(logN)

class Solution:
    def isHappy(self, n: int) -> bool:
        counter = n
        s = ''
        seen = set()
        while True:
            if counter == 1:
                return True
            elif counter in seen:
                return False
            else:
                seen.add(counter)
                s = str(counter)
                counter = 0
                for x in s:
                    counter += int(x) ** 2

# Floyd's Cycle-Finding Algorithm
# Time Complexity: O(logN)
# Space Complexity: O(1)

class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total += digit ** 2
            return total
        slow = n
        fast = get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return fast == 1