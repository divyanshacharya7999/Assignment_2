SELECT *, ROW_NUMBER() OVER(ORDER BY First_Name) AS RowID FROM Tables.USERS;


WITH USERS AS
(
   SELECT *, ROW_NUMBER()OVER(PARTITION BY ID ORDER BY ID) AS RowNumber
   FROM Tables.USERS
)
DELETE FROM USERS WHERE RowNumber > 1

SELECT * FROM Tables.USERS
