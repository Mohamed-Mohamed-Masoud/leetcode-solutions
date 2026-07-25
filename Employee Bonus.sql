-- Intuition
-- To find employees with a bonus less than 1000 or no bonus at all, 
-- we must ensure that employees without a matching record in the Bonus table are not excluded.
-- A LEFT JOIN is the intuitive choice to preserve all employee records regardless of their bonus status.

-- Approach
-- 1. Use a `LEFT JOIN` to combine the `Employee` table with the `Bonus` table based on `empId`.
-- 2. Apply a `WHERE` clause to filter the results.
-- 3. Explicitly check for `B.bonus < 1000` to get those with small bonuses, and `B.bonus IS NULL` to include employees who do not exist in the Bonus table. This approach avoids using functions on the column (like `IFNULL` or `COALESCE`), keeping the query index-friendly (SARGable) and optimized for performance.

-- Code
SELECT E.name, B.bonus
FROM Employee E
LEFT JOIN Bonus B ON E.empId = B.empId
WHERE B.bonus < 1000 OR B.bonus IS NULL;