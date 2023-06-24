# USED_GOODS_BOARD BOARD_ID, WRITER_ID, TITLE, CONTENTS, PRICE, CREATED_DATE, STATUS, VIEWS
#                  게시글 ID, 작성자 ID, 게시글 제목, 게시글 내용, 가격, 작성일,     거래상태, 조회수
# USED_GOODS_FILE USER_ID, NICKNAME, CITY, STREET_ADDRESS1, STREET_ADDRESS2, TLNO
#                  회원 ID, 닉네임,     시, 도로명 주소,          상세 주소,     전화번호

select u.user_id, u.nickname, sum(b.price) as total_sales
from (
    select writer_id, price, status
    from used_goods_board
    where status = "DONE") as b
inner join used_goods_user as u
on b.writer_id = u.user_id
group by u.user_id
having sum(b.price) >= 700000 
order by 3;