SELECT 
    player_id,
    event_date AS first_login
FROM
    Activity
WHERE 
    (player_id, event_date) IN(
        SELECT player_id, MIN(event_date)
        FROM Activity
        GROUP BY player_id
    );