-- Intuition:
-- We need to find salespersons who have NEVER placed an order
-- with the company named 'RED'.
-- Instead of finding the salespersons we want directly,
-- we first identify the salespersons who have orders with RED,
-- then exclude them from the final result.

-- Approach:
-- 1. The innermost subquery searches the Company table
--    to get the com_id of the company named 'RED'.

-- 2. The middle subquery searches the Orders table
--    to find all sales_id values associated with that com_id.
--    These are the salespersons who have orders with RED.

-- 3. The outer query retrieves salesperson names from SalesPerson.

-- 4. NOT IN excludes every sales_id returned by the subquery,
--    leaving only salespersons who have no orders with RED.

SELECT
    name
FROM
    SalesPerson
WHERE
    sales_id NOT IN(
        SELECT sales_id FROM Orders
        WHERE com_id IN(
            SELECT com_id FROM Company
            WHERE name = 'RED'
        )
    );