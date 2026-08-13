/*
Intuition
To find the sales information for the first year a product was sold, we need to determine the earliest sales year for each product. 
By filtering the table to match both the product ID and its corresponding minimum year, we can retrieve the exact quantity and price for that specific first year.

Approach
1. Use a subquery to group the `Sales` table by `product_id` and find the earliest sales year (`MIN(year)`) for each product.
2. In the main query, use a composite `IN` clause `(product_id, year) IN (...)` to filter the `Sales` table. This ensures we only select the rows that exactly match both the product ID and its first year identified in the subquery.
3. Select the requested columns, aliasing the `year` column as `first_year` to match the expected output.

Code
*/
SELECT
    product_id,
    year AS first_year,
    quantity,
    price
FROM
    Sales
WHERE
    (product_id, year) IN (SELECT product_id, MIN(year) FROM Sales GROUP BY product_id);
