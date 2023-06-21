-- 코드를 입력하세요
select car_id, round(avg(datediff(end_date, start_date) + 1),1) as average_duration 
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
group by car_id
having round(avg(datediff(end_date, start_date) + 1), 1) >= 7
order by 2 desc, 1 desc;