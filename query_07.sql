select s.student_name, g.grade, g.date
from students s
join grades g on s.student_id = g.student_id
where s.group_id = 1 and g.subject_id = 2;