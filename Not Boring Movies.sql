-- Intuition:
-- We need to find cinema movies that have an odd ID
-- and are NOT described as 'boring'.
-- After filtering, we want to display the highest-rated
-- movies first.

-- Approach:
-- 1. SELECT * to retrieve all columns from the Cinema table.
-- 2. Use WHERE to filter rows based on two conditions.
-- 3. id MOD 2 = 1 checks whether the ID is odd.
--    If the remainder after dividing by 2 is 1, the ID is odd.
-- 4. description != 'boring' excludes movies whose description
--    is exactly 'boring'.
-- 5. Use AND because both conditions must be satisfied.
-- 6. ORDER BY rating DESC sorts movies from highest
--    rating to lowest rating.

SELECT
    *
FROM
    Cinema
WHERE
    id MOD 2 = 1 AND
    description != 'boring'
ORDER BY
    rating DESC;