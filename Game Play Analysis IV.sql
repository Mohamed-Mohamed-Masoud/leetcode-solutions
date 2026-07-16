SELECT
    ROUND(COUNT(DISTINCT A1.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM
    Activity A1, Activity A2
WHERE
    DATEDIFF(A1.event_date, A2.event_date) = 1 AND
    A1.player_id  = A2.player_id AND
    (A2.player_id, A2.event_date) IN (
        SELECT player_id, MIN(event_date)
        FROM Activity
        GROUP BY player_id);