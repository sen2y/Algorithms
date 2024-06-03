-- 코드를 입력하세요
-- 동물의 이름은 몇 개인지 조회
SELECT COUNT(NAME)
FROM (SELECT NAME, COUNT(*) AS CNT
      FROM ANIMAL_INS
      GROUP BY NAME) AS SUB

