-- 코드를 입력하세요
-- USED_GOODS_BOARD와 USED_GOODS_REPLY 테이블에서 2022년 10월에 작성된 
-- 게시글 제목, 게시글 ID, 댓글 ID, 댓글 작성자 ID, 댓글 내용, 댓글 작성일
SELECT board.TITLE, board.BOARD_ID, reply.REPLY_ID, reply.WRITER_ID, reply.CONTENTS, DATE_FORMAT(reply.CREATED_DATE, '%Y-%m-%d') CREATED_DATE
FROM USED_GOODS_BOARD board, USED_GOODS_REPLY reply
WHERE board.BOARD_ID = reply.BOARD_ID
AND MONTH(board.CREATED_DATE) =10
AND YEAR(board.CREATED_DATE) =2022
ORDER BY reply.CREATED_DATE, board.TITLE;