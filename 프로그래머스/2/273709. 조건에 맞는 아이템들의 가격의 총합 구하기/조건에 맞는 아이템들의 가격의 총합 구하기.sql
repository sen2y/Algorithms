-- 코드를 작성해주세요
-- 아이템들의 가격의 총합 컬럼명은 'TOTAL_PRICE'
-- 희귀도가 'LEGEND'인 아이템들
SELECT SUM(PRICE) AS TOTAL_PRICE
FROM ITEM_INFO
WHERE RARITY = 'LEGEND'