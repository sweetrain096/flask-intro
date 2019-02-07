-- 테이블 값 모두 가져오기
SELECT * FROM classmates;

-- 특정 column만 가져오기
SELECT id, name FROM classmates;

--가져오는 row(레코드)의 갯수 지정
SELECT * FROM classmate LIMIT 3;

--가져오는 row(레코드)의 시작점을 지정하기
SELECT * FROM classmates LIMIT 5 OFFSET 2;