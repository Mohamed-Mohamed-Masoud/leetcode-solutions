-- Intuition:
-- We need to find countries that meet at least one of two conditions:
-- 1. Have a population of at least 25 million.
-- 2. Have an area of at least 3 million square kilometers.
-- A country qualifies if either condition is true.

-- Approach:
-- 1. SELECT name, population, area to retrieve the required information.
-- 2. Use WHERE to filter countries based on the given conditions.
-- 3. Use OR because satisfying either condition is enough.
-- 4. Use >= because the threshold values are included.

SELECT
    name, population, area
FROM
    World
WHERE
    population >= 25000000 OR
    area >= 3000000;