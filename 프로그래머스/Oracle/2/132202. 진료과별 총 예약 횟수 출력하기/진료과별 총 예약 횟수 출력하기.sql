-- 별칭에 공백이나 특수문자가 들어가면 반드시!! "" 사용
SELECT MCDP_CD AS "진료과 코드", COUNT(*) AS "5월예약건수"
FROM APPOINTMENT 
WHERE TO_CHAR(APNT_YMD, 'YYYY-MM') = '2022-05'
GROUP BY MCDP_CD
ORDER BY "5월예약건수", "진료과 코드"