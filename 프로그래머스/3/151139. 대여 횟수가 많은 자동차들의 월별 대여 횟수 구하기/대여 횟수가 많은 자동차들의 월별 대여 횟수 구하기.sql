# CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블에서 대여 시작일을 기준으로 2022년 8월부터 2022년 10월까지 총 대여 횟수가 5회 이상인 자동차들에 대해서 해당 기간 동안의 월별 자동차 ID 별 총 대여 횟수(컬럼명: RECORDS) 리스트를 출력하는 SQL문을 작성해주세요. 특정 월의 총 대여 횟수가 0인 경우에는 결과에서 제외해주세요

SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE '2022-08-01' <= START_DATE AND START_DATE <= '2022-10-31' and CAR_ID in (select CAR_ID
               from CAR_RENTAL_COMPANY_RENTAL_HISTORY
               where START_DATE between '2022-08-01' and '2022-10-31'
               group by CAR_ID
            HAVING COUNT(CAR_ID) >= 5)
GROUP BY MONTH, CAR_ID
HAVING RECORDS > 0
ORDER BY MONTH ASC, CAR_ID DESC