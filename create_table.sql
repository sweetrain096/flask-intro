-- create_table.sql
-- AUTOINCREMENT는 INTEGER에만 지정 가능.
-- NOT NULL : INSERT에서 반드시 값이 있어야한다.
CREATE TABLE classmates (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
);