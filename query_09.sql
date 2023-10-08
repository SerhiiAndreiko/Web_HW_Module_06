select s.subject_name
from students st
join grades g on st.student_id = g.student_id
join subjects s on g.subject_id = s.subject_id
where st.student_id = 12;