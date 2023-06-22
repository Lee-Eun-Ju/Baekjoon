-- BOARD_ID, WRITER_ID, TITLE, CONTENTS, PRICE, CREATED_DATE, STATUS, VIEWS
-- 게시글 ID, 작성자 ID, 게시글 제목, 게시글 내용, 가격, 작성일, 거래상태, 조회수

-- USER_ID, NICKNAME, CITY, STREET_ADDRESS1, STREET_ADDRESS2, TLNO
-- 회원 ID, 닉네임, 시, 도로명 주소, 상세 주소, 전화번호

select u.user_id, u.nickname, 
concat(u.CITY, " ", u.STREET_ADDRESS1, " ", u.STREET_ADDRESS2) as 전체주소, 
concat(left(u.tlno, 3), "-",
       mid(u.tlno, 4,4), "-",
       right(u.tlno,4)) as 전화번호
from used_goods_board as b
inner join used_goods_user as u
on b.writer_id = u.user_id
group by b.writer_id
having count(board_id)>=3
order by u.user_id desc;