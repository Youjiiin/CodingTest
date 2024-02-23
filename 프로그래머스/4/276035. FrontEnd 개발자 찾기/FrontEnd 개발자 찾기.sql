-- 코드를 작성해주세요
SELECT DISTINCT D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
FROM SKILLCODES S
JOIN DEVELOPERS D
ON S.CODE & D.SKILL_CODE > 0 
WHERE S.CATEGORY = 'Front End'
ORDER BY D.ID