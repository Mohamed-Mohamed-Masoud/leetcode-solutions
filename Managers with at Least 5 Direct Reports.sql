# Intuition
# This query finds all employees who are managers and have at least 5 direct reports.

# Approach
# 1. We first create a subquery that selects the managerId from the Employee table
# 2. We group the results by managerId and use the HAVING clause to filter for managers with at least 5 direct reports.
# 3. We then join the Employee table with the subquery on the managerId to get the names of those managers.

# Performance Optimization
# I used JOiN instead of a WHERE IN clause for better performance.

# CODE
SELECT e.name 
FROM Employee e
JOIN (
    SELECT managerId 
    FROM Employee
    GROUP BY managerId 
    HAVING COUNT(managerId) >= 5
    ) AS m ON e.id = m.managerId;