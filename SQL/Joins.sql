--Basic Syntax for different joins in SQL
------------------------------------------------

--Inner Join: includes rows from each table where there is matching data (intersect).
SELECT a.ColumnName b.ColumnName
FROM TableName a
INNER JOIN TableName b ON a.ColumnName = b.ColumnName;


--Left Outer Join: Includes all rows from the table on the left, and matching rows from the table on the right.
SELECT a.ColumnName b.ColumnName
FROM TableName a
LEFT JOIN TableName b ON a.ColumnName = b.ColumnName;


--Right Outer Join: Includes all rows from the table on the right, and matching rows from the table on the left.
SELECT a.ColumnName b.ColumnName
FROM TableName a
RIGHT JOIN TableName b ON a.ColumnName = b.ColumnName;


--Full Outer Join: Includes all rows from both tables, regardless of whether they have matches or not.
SELECT a.ColumnName b.ColumnName
FROM TableName a
FULL OUTER JOIN TableName b ON a.ColumnName = b.ColumnName;


--Union: Combines the results of two queries into one table (only shows distinct values; must have same number of columns, same names, same order, same data types)
SELECT ColumnNames FROM TableName
UNION
SELECT ColumnNames FROM TableName;


--Union All: Combines the results of two queries into one table (shows all values; must have same number of columns, same names, same order, same data types)
SELECT ColumnNames FROM TableName
UNION ALL 
SELECT ColumnNames FROM TableName;