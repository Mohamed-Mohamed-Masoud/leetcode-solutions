SELECT E.name AS Employee
FROM Employee E
JOIN Employee M ON E.managerId = M.id
Where E.salary > M.salary;