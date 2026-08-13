/*
Intuition:
The goal is to find the total number of orders placed by each user specifically in the year 2019. We need to include all users in the final result, even if they didn't make any orders that year, which makes a LEFT JOIN from the Users table the perfect choice.

Approach:
1. Start with the `Users` table to ensure every user is included in the output.
2. Perform a `LEFT JOIN` with the `Orders` table on the user ID.
3. Crucially, apply the date filter `YEAR(O.order_date) = 2019` directly inside the `ON` clause. If we placed this in a `WHERE` clause, it would filter out users with zero orders in 2019 (acting like an INNER JOIN).
4. Group the results by `user_id` and `join_date`.
5. Use `COUNT(O.order_id)` to count the valid orders. Users with no 2019 orders will have NULL for `O.order_id`, resulting in a count of 0.
6. Order the final result by `user_id` (buyer_id).
*/

SELECT 
    U.user_id AS buyer_id,
    U.join_date,
    COUNT(O.order_id) AS orders_in_2019
FROM
    Users U
LEFT JOIN
    ORDERS O ON U.user_id = O.buyer_id AND YEAR(O.order_date) = 2019
GROUP BY
    U.user_id,
    U.join_date
ORDER BY
    U.user_id;