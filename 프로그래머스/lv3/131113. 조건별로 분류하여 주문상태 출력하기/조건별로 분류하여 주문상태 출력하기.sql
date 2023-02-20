-- 코드를 입력하세요
SELECT ORDER_ID, PRODUCT_ID, left(OUT_DATE, 10) as OTU_DATE, case when left(OUT_DATE, 10) <= '2022-05-01' then '출고완료' when OUT_DATE is null then '출고미정' else '출고대기'  end as '출고여부'
FROM FOOD_ORDER
ORDER BY ORDER_ID