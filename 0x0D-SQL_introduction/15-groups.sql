-- script that lists the number of records with the same score in the table
SELECT score, COUNT(*) as number from second_table group by score
