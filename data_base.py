import sqlite3

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        group_id INTEGER,
        FOREIGN KEY(group_id) REFERENCES groups(id)
    )
''')

cursor.execute('''
    CREATE TABLE groups (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE teachers (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE subjects (
        id INTEGER PRIMARY KEY,
        name TEXT,
        teacher_id INTEGER,
        FOREIGN KEY(teacher_id) REFERENCES teachers(id)
    )
''')

cursor.execute('''
    CREATE TABLE grades (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        subject_id INTEGER,
        grade INTEGER,
        date DATE,
        FOREIGN KEY(student_id) REFERENCES students(id),
        FOREIGN KEY(subject_id) REFERENCES subjects(id)
    )
''')

conn.commit()
conn.close()
