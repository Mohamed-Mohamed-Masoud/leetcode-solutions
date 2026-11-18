-- Intuition:
-- We need to swap the gender values in the Salary table:
-- 'm' becomes 'f', and 'f' becomes 'm'.
-- Every row must be updated, not just selected rows.

-- Approach:
-- 1. UPDATE Salary to modify the existing records.
-- 2. SET sex = CASE to apply conditional logic to each row.
-- 3. WHEN sex = 'm' THEN 'f' changes male to female.
-- 4. ELSE 'm' changes all remaining values (female) to male.
-- 5. No WHERE clause is needed because we want to update every row.

UPDATE
    Salary
SET sex =
    CASE
        WHEN sex = 'm' THEN 'f'
        ELSE 'm'
    END;