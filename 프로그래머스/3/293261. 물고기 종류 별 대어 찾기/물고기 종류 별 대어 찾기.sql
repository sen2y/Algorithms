-- 코드를 작성해주세요
-- 물고기의 ID, 물고기 이름, 길이를 출력
-- 물고기의 ID 컬럼명은 ID, 이름 컬럼명은 FISH_NAME, 길이 컬럼명은 LENGTH
-- 물고기 종류 별로 가장 큰 물고기
-- 물고기의 ID에 대해 오름차순 정렬
SELECT ID, FISH_NAME, LENGTH
FROM FISH_INFO AS I
JOIN FISH_NAME_INFO AS N ON I.FISH_TYPE = N.FISH_TYPE
WHERE I.LENGTH = (
    SELECT MAX(LENGTH) -- 서브쿼리: 각 물고기 종류의 최대 길이를 구함
    FROM FISH_INFO AS I2
    WHERE I2.FISH_TYPE = I.FISH_TYPE) -- 해당 물고기 종류의 최대 길이를 가진 레코드만 선택
ORDER BY I.ID