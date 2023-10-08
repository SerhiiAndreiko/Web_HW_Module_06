import sqlite3
from faker import Faker
import random
from datetime import date

# Create connect with db
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

fake = Faker()

# Generic group
groups = ["Group A", "Group B", "Group C"]
for group in groups:
    cursor.execute("insert into groups (group_name) values (?)", (group,))
    conn.commit()

# Generic students
for _ in range(50):
    student_name = fake.name()
    group_id = random.randint(1, 3)
    cursor.execute("insert into students (student_name, group_id) values (?, ?)", (student_name, group_id))
    conn.commit()

# Generic teacher
teachers = [fake.name(), fake.name(), fake.name()]
for teacher in teachers:
    cursor.execute('insert into teachers (teacher_name) values (?)', (teacher,))
    conn.commit()

# Generic subjects
subjects = ['Math', 'Physics', 'Chemistry', 'History', 'Biology']
for subject in subjects:
    teacher_id = random.randint(1, 3)
    cursor.execute('insert into subjects (subject_name, teacher_id) values (?, ?)', (subject, teacher_id))
    conn.commit()

# Generic grade
for student_id in range(1, 51):
    for subject_id in range(1, 6):
        num_grades = random.randint(2, 20)
        for _ in range(num_grades):
            grade = round(random.uniform(2, 5), 1)
            date_received = fake.date_between(start_date='-1y', end_date='today')
            cursor.execute('insert into grades (student_id, subject_id, grade, date) values (?, ?, ?, ?)',
                           (student_id, subject_id, grade, date_received))
            conn.commit()

# Close connection
conn.close()