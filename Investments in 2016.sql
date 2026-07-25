-- Intuition
-- To ensure a location is strictly unique to one policyholder, 
-- latitude and longitude must be evaluated together as a single coordinate pair. 
-- Checking them independently could incorrectly exclude distinct locations that only happen to share one axis.

-- Approach
-- Filter the records by ensuring the `tiv_2015` value is shared by at least one other record using an `IN` clause.
-- Then, use a tuple `(lat, lon)` in the `WHERE` clause with a `NOT IN` condition against a subquery that groups by both coordinates. 
-- This guarantees we only include individuals whose exact geographic pair does not repeat in the dataset.

-- Code
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (SELECT tiv_2015 FROM Insurance GROUP BY tiv_2015 HAVING COUNT(tiv_2015) > 1) AND
    (lat, lon) NOT IN (SELECT lat, lon FROM Insurance GROUP BY lat, lon HAVING COUNT(lat) > 1 AND COUNT(lon) > 1);