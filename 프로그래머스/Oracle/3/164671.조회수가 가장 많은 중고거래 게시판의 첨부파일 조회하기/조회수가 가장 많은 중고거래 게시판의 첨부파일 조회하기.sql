-- 1. 조회수가 가장 높은 중고거래 게시물 찾기(하나만 존재)
-- 2. 첨부파일 경로 조회('/home/grep/src/'+게시글ID+파일ID+파일이름+파일확장자)
-- 3. 첨부파일 경로는 FILE ID를 기준으로 내림차순 정렬
SELECT ('/home/grep/src/' || B.BOARD_ID || '/' || F.FILE_ID || F.FILE_NAME || F.FILE_EXT) AS FILE_PATH
FROM USED_GOODS_BOARD B INNER JOIN USED_GOODS_FILE F
     ON B.BOARD_ID = F.BOARD_ID
WHERE B.VIEWS = (SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
ORDER BY F.FILE_ID DESC;