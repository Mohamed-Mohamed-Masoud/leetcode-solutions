"""
Intuition
To find the user with the most friends, we must count every time a user is part of an accepted request. Since a user can be either the one who sent the request or the one who accepted it, we need to look at both columns combined.

Approach
Use UNION ALL to merge both requester_id and accepter_id into a single, unified list of IDs.

Group this combined list by id.

Use COUNT(*) to calculate the total number of friends for each user.

Sort the results in descending order based on the count (ORDER BY num DESC).

Use LIMIT 1 to extract only the top user with the highest number of friends.

Code
"""
SELECT id, COUNT(*) AS num
FROM
    (SELECT requester_id as id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id FROM RequestAccepted) AS TEMP
GROUP BY id
ORDER BY num DESC
LIMIT 1;