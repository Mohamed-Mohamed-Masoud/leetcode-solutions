-- Intuition:
-- We need to find the customer who placed the highest number of orders.
-- Each row represents an order, so counting rows for each customer
-- tells us how many orders that customer placed.

-- Approach:
-- 1. GROUP BY customer_number to group all orders belonging to the same customer.
-- 2. COUNT(*) to calculate the total number of orders for each customer.
-- 3. ORDER BY COUNT(*) DESC to sort customers from highest to lowest order count.
-- 4. LIMIT 1 to return only the customer with the most orders.

SELECT
    customer_number
FROM
    Orders
GROUP BY
    customer_number
ORDER BY
    COUNT(*) DESC
LIMIT 1;