select st.group_id, g.group_name, avg(gd.grade) as avg_grade
from students st
join groups g on st.group_id = g.group_id
join grades gd on st.student_id = gd.student_id
where gd.subject_id = 1
group by st.group_id, g.group_name;