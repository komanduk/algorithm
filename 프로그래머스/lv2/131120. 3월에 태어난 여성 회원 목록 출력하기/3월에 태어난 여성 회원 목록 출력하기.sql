-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, left(DATE_OF_BIRTH, 10)
FROM MEMBER_PROFILE
WHERE GENDER = 'W' AND DATE_OF_BIRTH LIKE ('____-%03-__') AND TLNO IS NOT NULL
ORDER BY MEMBER_ID