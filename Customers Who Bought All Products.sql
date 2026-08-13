/*
Intuition
To identify customers who purchased every product, we can count the number of unique products each customer bought. 
If this count matches the total number of products available in the catalog, it means the customer has bought all of them.

Approach
1. Group the `Customer` table by `customer_id` using `GROUP BY` to analyze each customer's purchases.
2. Use `COUNT(DISTINCT product_key)` to find the number of unique products each customer bought.
3. Use a subquery `(SELECT COUNT(*) FROM Product)` to determine the total number of products available.
4. Use the `HAVING` clause to filter and return only the customers whose unique purchase count matches the total product count.

Code
*/

SELECT 
    customer_id
FROM
    Customer
GROUP BY
    customer_id
HAVING
    COUNT(DISTINCT product_key) IN (SELECT COUNT(*) FROM Product);