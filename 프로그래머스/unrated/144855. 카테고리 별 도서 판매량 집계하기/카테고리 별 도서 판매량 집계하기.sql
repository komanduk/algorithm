-- 코드를 입력하세요
SELECT t1.CATEGORY, sum(t2.SALES) as TOTAL_SALES
FROM BOOK as t1
INNER JOIN BOOK_SALES as t2
ON t1.BOOK_ID = t2.BOOK_ID
WHERE t2.sales_date LIKE '%2022-01-__%'
GROUP BY t1.category
ORDER BY t1.category