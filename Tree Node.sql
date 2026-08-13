/*
Intuition
To classify each node in a tree, we can determine its position by checking its parent ID (p_id) and seeing whether it serves as a parent to any other nodes in the table.

Approach
1. Use a CASE statement to evaluate conditions sequentially for each node.
2. Root: If a node has no parent (p_id IS NULL), it is the root of the tree.
3. Inner: If a node's id is present in the p_id column of the table (id IN (SELECT p_id FROM Tree)), it means it has children, making it an inner node.
4. Leaf: If neither of the above conditions is met, the node has a parent but no children, meaning it is a leaf node.

Code
*/
SELECT
    id,
    CASE
        WHEN p_id is null THEN 'Root'
        WHEN id in (SELECT p_id FROM TREE) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree;