-- 코드를 입력하세요
SELECT
    floor(price/10000)*10000 as price_group
    , count(product_id)
from product
GROUP BY price_group
ORDER BY price_group