-- 코드를 입력하세요
SELECT t1.FLAVOR
FROM FIRST_HALF AS t1
INNER JOIN ICECREAM_INFO AS t2
ON t1.FLAVOR = t2.FLAVOR
WHERE TOTAL_ORDER >= '3000' AND INGREDIENT_TYPE = 'fruit_based'
ORDER BY TOTAL_ORDER DESC