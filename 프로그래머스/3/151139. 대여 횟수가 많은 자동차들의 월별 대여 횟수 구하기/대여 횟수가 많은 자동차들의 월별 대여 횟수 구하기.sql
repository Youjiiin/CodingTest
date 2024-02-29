-- 코드를 입력하세요
SELECT MONTH(START_DATE) MONTH, CAR_ID, COUNT(HISTORY_ID) RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' AND  '2022-11' 
AND CAR_ID IN (SELECT CAR_ID
              FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
              WHERE DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' AND  '2022-11' 
              GROUP BY CAR_ID
              HAVING COUNT(*) >= 5)
GROUP BY CAR_ID, MONTH(START_DATE)
HAVING RECORDS >= 1
ORDER BY MONTH(START_DATE), CAR_ID DESC