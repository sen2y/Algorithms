-- 코드를 입력하세요
-- 동물의 아이디와 이름을 조회
-- 아픈 동물
-- 결과는 아이디 순으로 조회
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'
ORDER BY ANIMAL_ID