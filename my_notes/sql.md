PostgreSQL  MySQL            SQLite
----------- ---------------- ------
\l          SHOW databases;  
\dt         SHOW tables;     SELECT name FROM sqlite_master WHERE type='table'
\c DB       USE DB;
			     PRAGMA table_info(table_name)  #get columns
CREATE DATABASE DB;
DROP DATABASE DB;

CREATE TABLE my_table(
    id INTEGER PRIMARY KEY,
    name TEXT
);
DROP TABLE my_table;

SELECT a, b+c FROM my_table;

INSERT INTO my_table(id, name) VALUES(1, 'Ben');
UPDATE my_table SET name='Sarah' WHERE id=1;
DELETE FROM my_table WHERE id=1;
