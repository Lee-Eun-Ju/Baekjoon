select car_id, 
      max(if(start_date <= date("2022-10-16") and end_date >= date("2022-10-16"),
      "대여중", "대여 가능")) as availability
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
order by car_id desc;