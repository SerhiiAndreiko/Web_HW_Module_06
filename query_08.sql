select t.teacher_name, avg(g.grade) as avg_grade
from teachers t
join subjects s on t.teacher_id = s.teacher_id
join grades g on s.subject_id = g.subject_id
where t.teacher_id = 1
group by t.teacher_name;