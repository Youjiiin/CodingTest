-- 코드를 입력하세요
SELECT YEAR(O.SALES_DATE) YEAR, MONTH(O.SALES_DATE) MONTH, I.GENDER, COUNT(DISTINCT(I.USER_ID)) USERS
FROM USER_INFO I
    JOIN ONLINE_SALE O
    ON I.USER_ID = O.USER_ID
WHERE I.GENDER IS NOT NULL
GROUP BY YEAR(O.SALES_DATE), MONTH(O.SALES_DATE), I.GENDER
ORDER BY YEAR(O.SALES_DATE), MONTH(O.SALES_DATE), I.GENDER