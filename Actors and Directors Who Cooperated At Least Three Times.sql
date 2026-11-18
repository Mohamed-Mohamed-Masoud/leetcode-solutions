-- Intuition:
-- We need to find pairs of actors and directors who have
-- collaborated on at least 3 movies.
-- Each row represents a collaboration between an actor and a director.
-- We need to count how many times each unique pair appears.

-- Approach:
-- 1. GROUP BY actor_id, director_id to group records
--    based on the unique combination of actor and director.
-- 2. COUNT(*) calculates how many collaborations each pair has.
-- 3. HAVING COUNT(*) >= 3 filters the groups to keep
--    only pairs that appear at least 3 times.
-- 4. Return the actor_id and director_id of qualifying pairs.

SELECT
    actor_id, director_id
FROM
    ActorDirector
GROUP BY
    actor_id, director_id
HAVING
    COUNT(*) >= 3;