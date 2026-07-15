SELECT email AS Email
FROM Person
GROUP BY email
Having COUNT(email) > 1;