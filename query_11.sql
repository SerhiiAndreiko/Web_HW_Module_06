select t.teacher_id, s.student_id, avg(g.grade) as avg_grade
from teachers t
join subjects sb on t.teacher_id = sb.teacher_id
join grades g on sb.subject_id = g.subject_id
join students s on g.student_id = s.student_id
where t.teacher_id = 1 and s.student_id = 5
group by t.teacher_id, s.student_id;
