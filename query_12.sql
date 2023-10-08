with last_class as (
    select student_id, max(date) as last_date
    from grades
    where subject_id = 2
    group by student_id
)

select s.student_name, g.grade, g.date
from last_class lc
join grades g on lc.student_id = g.student_id and lc.last_date = g.date
join students s on lc.student_id = s.student_id
where s.group_id = 3 and g.subject_id = 2;