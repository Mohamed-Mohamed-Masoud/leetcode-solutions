SELECT
    D.name AS Department,
    E.name AS Employee,
    E.salary AS Salary
FROM
    Employee E
JOIN
    Department D ON E.departmentId = D.id
WHERE
    (E.departmentId, Salary) IN 
        (SELECT 
            departmentId, salary
        FROM (SELECT 
                departmentId, salary,
                DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) AS salary_rank
            FROM Employee) AS TempTable
        WHERE salary_rank <= 3);