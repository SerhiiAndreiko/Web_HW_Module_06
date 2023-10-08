select s.subject_name
from students st
join grades g on st.student_id = g.student_id
join subjects s on g.subject_id = s.subject_id
join teachers t on s.teacher_id = t.teacher_id
where st.student_id = 10 and t.teacher_id = 3;