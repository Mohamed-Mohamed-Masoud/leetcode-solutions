"""
Intuition
Instead of trying to swap student names using complex functions, a simpler and more performant idea is to mathematically swap the seat numbers (id). Even seat numbers become odd, and odd ones become even, with the exception of the last student if the total number of students is odd, keeping them in their original place.

Approach
We use a CASE statement to modify the id value for each student based on the following rules:
1. If the id is even (id % 2 = 0), we subtract 1 (id - 1) to move them back one seat.
2. If the id is the highest number in the table (the last student), we leave it unchanged (id) since there is no next student to swap with.
3. Otherwise (a regular odd id), we add 1 (id + 1) to move them forward one seat.
4. Finally, we sort the result set based on the newly calculated id using ORDER BY id.

Code
"""
SELECT
    CASE
        WHEN id % 2 = 0 THEN id - 1
        WHEN id IN (SELECT MAX(id) FROM Seat) THEN id
        ELSE id + 1
    END AS id,
    student
FROM
    Seat
ORDER BY id;