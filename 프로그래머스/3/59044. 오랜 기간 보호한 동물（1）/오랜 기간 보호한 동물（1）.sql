# 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 시작일 순으로 조회해야 합니다.

SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS I # 보호소에 들어온 동물 저보 테이블
LEFT JOIN ANIMAL_OUTS O # 입양 보낸 동물 테이블
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.DATETIME IS NULL
ORDER BY I.DATETIME
LIMIT 3