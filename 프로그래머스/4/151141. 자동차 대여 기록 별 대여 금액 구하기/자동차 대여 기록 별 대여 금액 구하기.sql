-- 코드를 입력하세요
SELECT B.HISTORY_ID, 
ROUND(DAILY_FEE * (DATEDIFF(B.END_DATE, B.START_DATE)+1) * (CASE 
WHEN DATEDIFF(END_DATE, START_DATE) + 1 < 7 THEN 1
WHEN DATEDIFF(END_DATE, START_DATE) + 1 < 30 THEN 0.95
WHEN DATEDIFF(END_DATE, START_DATE) + 1 < 90 THEN 0.92 
ELSE 0.85 END)) AS FEE
FROM CAR_RENTAL_COMPANY_CAR A
    JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY B
    ON A.CAR_ID = B.CAR_ID
    JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN C
    ON A.CAR_TYPE = C.CAR_TYPE
WHERE A.CAR_TYPE LIKE '%트럭%'
GROUP BY B.HISTORY_ID
ORDER BY FEE DESC, B.HISTORY_ID DESC