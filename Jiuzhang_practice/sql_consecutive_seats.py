select distinct t2.seat_id
from cinema as t1, cinema as t2
where (t1.seat_id = t2.seat_id-1 and t1.free=1 and t2.free=1) or (t1.seat_id-1 = t2.seat_id and t1.free=1 and t2.free=1)
order by t2.seat_id
