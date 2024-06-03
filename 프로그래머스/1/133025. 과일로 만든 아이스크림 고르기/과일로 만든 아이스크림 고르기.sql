-- 코드를 입력하세요
-- 아이스크림의 맛
-- 아이스크림 총주문량이 3,000보다 높으면서 아이스크림의 주 성분이 과일인 아이스크림의 맛
-- 총주문량이 큰 순서대로 조회
SELECT F.FLAVOR
FROM FIRST_HALF AS F
JOIN ICECREAM_INFO AS I ON F.FLAVOR = I.FLAVOR
WHERE TOTAL_ORDER > 3000 AND I.INGREDIENT_TYPE = 'fruit_based'
ORDER BY TOTAL_ORDER DESC;