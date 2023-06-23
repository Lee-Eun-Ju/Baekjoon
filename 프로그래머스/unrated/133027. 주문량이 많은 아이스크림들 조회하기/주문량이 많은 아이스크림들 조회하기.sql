-- FIRST_HALF : SHIPMENT_ID, FLAVOR, TOTAL_ORDER 상반기
-- JULY : SHIPMENT_ID, FLAVOR, TOTAL_ORDER 7월

select f.flavor
from (
    select flavor, sum(total_order) as total_order
    from first_half
    group by flavor) as f
inner join (
    select flavor, sum(total_order) as total_order
    from july
    group by flavor) as j
on f.flavor = j.flavor
order by f.total_order + j.total_order desc
limit 3;