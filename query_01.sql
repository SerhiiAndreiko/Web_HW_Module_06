select s.student_id, s.student_name, avg(g.grade) as avg_grade
from students s
join grades g on s.student_id = g.student_id
group by s.student_id, s.student_name
order by avg_grade desc
limit 5;