-- Intuition:
-- We need to find classes that have at least 5 students enrolled.
-- Since multiple rows may belong to the same class,
-- we need to group rows by class and count the records in each group.

-- Approach:
-- 1. GROUP BY class to group all records belonging to the same class.
-- 2. COUNT(*) to calculate the number of students in each class.
-- 3. Use HAVING to filter groups based on their aggregate count.
-- 4. COUNT(*) >= 5 ensures that only classes with at least 5 students are returned.

SELECT
    class
FROM
    Courses
GROUP BY
    class
HAVING
    COUNT(*) >= 5;