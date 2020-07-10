
with table1 as
(select A.student_id, E.course_id, E.grade
from
(select student_id, max(grade) as grade
from Enrollments
group by student_id
order by max(grade) DESC) as A
left join Enrollments as E
on A.student_id = E.student_id and A.grade = E.grade)

select student_id, min(course_id) as course_id, grade
from table1
group by student_id, grade
order by student_id;


# window function 就是方便啊
select E.student_id, E.course_id, E.grade
from
    (select *, row_number() over (partition by student_id order by grade DESC, course_id) as rank_value
    from Enrollments) as E
where E.rank_value=1;
