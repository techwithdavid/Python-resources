--Basic Syntax for different table creation queries in SQL
-----------------------------------------------------------

--Create Table: Basic create statement to create a new table
CREATE NewTableName (
    ColumnName1 DataType,
    ColumnName2 DataType, 
    ColumnName3 DataType
);


--Create Table As: Create statement to create a table based on the results of another query
CREATE NewTableName AS 
SELECT ...
FROM OldTableName
...;


--Select Into: Similar to 'Create Table As'; Selects data from one table to a new table
SELECT ...
INTO NewTableName
FROM OldTableName
WHERE ...
...;