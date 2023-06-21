-- APNT_YMD,   APNT_NO,   PT_NO, MCDP_CD, MDDR_ID, APNT_CNCL_YN, APNT_CNCL_YMD
-- 진료예약일시, 진료예약번호, 환자번호, 진료과코드, 의사ID, 예약취소여부, 예약취소날짜
SELECT mcdp_cd as "진료과코드", count(apnt_no) as "5월예약건수"
from appointment
where date_format(apnt_ymd, "%Y-%m") ="2022-05" 
group by mcdp_cd
order by 2,1