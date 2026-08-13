/*
Intuition:
We need to determine the active price of each product on a specific date ('2019-08-16'). The active price is the one set by the most recent update on or before this date. If a product's very first price change occurred after this date, its price on that day must be the default value of 10.

Approach:
1. Divide the problem into two mutually exclusive cases and combine the results using `UNION`.
2. Case 1 (Updated before or on the target date): Use a subquery to find the most recent `change_date` (using `MAX(change_date)`) that is `<=` '2019-08-16' for each product. Match this exact date and `product_id` with the main table to fetch the corresponding `new_price`.
3. Case 2 (Never updated before or on the target date): Group the products and use a `HAVING` clause to find items where their earliest update (`MIN(change_date)`) is strictly `>` '2019-08-16'. Assign these products the default price of 10.
4. The `UNION` seamlessly merges these two sets to provide the comprehensive price list for all products on that date.
*/

SELECT
    product_id,
    new_price AS price
FROM
    Products
WHERE
    (product_id, change_date) IN
        (SELECT product_id, MAX(change_date)
        FROM Products
        WHERE change_date <= '2019-08-16'
        GROUP BY product_id)

UNION

SELECT
    product_id,
    10
FROM
    Products
GROUP BY
    product_id
HAVING
    MIN(change_date) > '2019-08-16';