-- Intuition:
-- We need to find the largest number that appears exactly once
-- in the MyNumbers table.
-- First, identify numbers that occur only once (unique numbers).
-- Then, find the maximum value among those numbers.
-- If no unique number exists, MAX() returns NULL.

-- Approach:
-- 1. GROUP BY num to group all identical numbers together.
-- 2. COUNT(num) calculates how many times each number appears.
-- 3. HAVING COUNT(num) = 1 filters groups to keep only numbers
--    that appear exactly once.
-- 4. Use the subquery (SingleNum) to create a temporary result
--    containing only unique numbers.
-- 5. MAX(num) selects the largest number from that result.
-- 6. AS num gives the final output column the name 'num'.

SELECT 
    MAX(num) AS num
FROM(
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
) AS SingleNum;