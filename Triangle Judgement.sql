-- Intuition:
-- We need to determine whether three given side lengths
-- can form a valid triangle.
-- A triangle is valid only if all sides are positive
-- and the sum of any two sides is greater than the third side.

-- Approach:
-- 1. SELECT x, y, z to retrieve the three side lengths.
-- 2. Use CASE to evaluate the conditions for each row.
-- 3. Check that all sides are positive (x > 0, y > 0, z > 0).
-- 4. Apply the Triangle Inequality Theorem:
--    - x + y > z
--    - y + z > x
--    - x + z > y
-- 5. Use AND because ALL conditions must be TRUE.
-- 6. If all conditions are satisfied, return 'Yes'.
--    Otherwise, return 'No'.
-- 7. AS triangle assigns the result column the name 'triangle'.

SELECT
    x, y, z,
    CASE
        WHEN
            x > 0 and
            y > 0 and
            z > 0 and
            (x + y) > z and
            (y + z) > x and
            (x + z) > y
        THEN 'Yes'
        ELSE 
            'No'
    END AS triangle
FROM
    Triangle;