-- Intuition
-- SQL inequality operators exclude `NULL` values by default. We must handle them explicitly to avoid missing records.

-- Approach
-- Use the `OR` operator in the `WHERE` clause to filter for `referee_id != 2` while explicitly including `referee_id IS NULL`.

# Code
SELECT name
FROM Customer
WHERE referee_id IS NULL OR referee_id != 2;