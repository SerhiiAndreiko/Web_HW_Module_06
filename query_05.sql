select t.teacher_name, s.subject_name
from teachers t
join subjects s on t.teacher_id = s.teacher_id
where t.teacher_id = 1;