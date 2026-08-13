/*
Intuition:
The objective is to calculate the percentage of customers whose very first order was an "immediate" delivery. An order is considered immediate if the order date matches the preferred delivery date. To solve this, we first need to isolate every customer's initial order, and then find the ratio of immediate orders within that specific group.

Approach:
1. Use a subquery to find the first order for each customer by grouping by `customer_id` and selecting the `MIN(order_date)`.
2. Filter the main `Delivery` table using the `WHERE (customer_id, order_date) IN (...)` clause to ensure we are only looking at the first orders for all customers.
3. Use a `CASE` statement inside a `SUM` function to count the number of immediate orders (returning 1 if `order_date = customer_pref_delivery_date`, else 0).
4. Multiply the sum of immediate orders by 100 and divide by the total count of first orders (`COUNT(*)`) to get the percentage.
5. Finally, use the `ROUND` function to format the result to 2 decimal places as `immediate_percentage`.
*/

SELECT
    ROUND(SUM(
        CASE
            WHEN order_date = customer_pref_delivery_date THEN 1
            ELSE 0
        END) * 100 / COUNT(*), 2) AS immediate_percentage 
FROM
    Delivery
WHERE
    (customer_id, order_date) IN
        (SELECT customer_id, MIN(order_date) FROM Delivery GROUP BY customer_id);