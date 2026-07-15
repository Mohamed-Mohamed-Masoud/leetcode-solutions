SELECT
    DISTINCT current_num AS ConsecutiveNums
FROM
    (SELECT
        num AS current_num,
        LEAD(num,1) over(ORDER BY id) AS next_num,
        LEAD(num,2) over(ORDER BY id) AS next_next_num
    FROM
        Logs) AS TEMPTABLE
WHERE
    current_num = next_num AND
    current_num = next_next_num;