select
table1.name as results
from
(select U.name
from
    (select user_id, count(movie_id) as num_ratings
     from Movie_Rating
        group by user_id) as A
    left join Users as U
    on A.user_id = U.user_id
    order by A.num_ratings DESC, U.name
    limit 1) table1
union
select *
from
    (select M.title
     from
     (select movie_id, avg(rating) as avg_ratings
      from Movie_Rating
       where created_at between DATDE("2020-02-01") and DATE("2020-02-29")
        group by movie_id ) as B
        left join Movies as M
        on B.movie_id = M.movie_id
        order by B.avg_ratings DESC, M.title
      limit 1) as table2;

# (table 1) union (table 2)
(select u.name as results
from
(select user_id, count(movie_id) as num_movies
from Movie_Rating
group by user_id) as t1
left join Users as u
on t1.user_id = u.user_id
order by t1.num_movies DESC, u.name
limit 1)
union

(select title
from
(select title, avg(rating) as avg_rating
from
(select r.movie_id, r.rating, r.created_at, m.title
from Movie_Rating as r
left join Movies as m
on m.movie_id = r.movie_id) as t2
where created_at between DATE("2020-02-01") and DATE("2020-02-29")
group by movie_id
order by avg_rating DESC, title) as t3
limit 1);
