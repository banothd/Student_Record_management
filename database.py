import sqlite3

DB_NAME = "students.db"


def connect_db():

    conn = sqlite3.connect(DB_NAME)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (

            student_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            course TEXT,
            marks REAL,
            grade TEXT
        )
    """)

    return conn


def add_student(student):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        student.student_id,
        student.name,
        student.age,
        student.course,
        student.marks,
        student.grade
    ))

    conn.commit()
    conn.close()


def get_students():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    data = cursor.fetchall()

    conn.close()

    return data

def search_student(student_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE student_id = ?",
        (student_id,)
    )

    data = cursor.fetchone()

    conn.close()

    return data 

def update_student(student):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE students
        SET name = ?,
            age = ?,
            course = ?,
            marks = ?,
            grade = ?
        WHERE student_id = ?
    """, (
        student.name,
        student.age,
        student.course,
        student.marks,
        student.grade,
        student.student_id
    ))

    conn.commit()
    conn.close()

def delete_student(student_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE student_id = ?",
        (student_id,)
    )

    conn.commit()
    conn.close()

def get_total_students():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")

    total = cursor.fetchone()[0]

    conn.close()

    return total

def get_marks_statistics():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            AVG(marks),
            MAX(marks),
            MIN(marks)
        FROM students
    """)

    stats = cursor.fetchone()

    conn.close()

    return stats

def get_grade_distribution():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT grade, COUNT(*)
        FROM students
        GROUP BY grade
    """)

    data = cursor.fetchall()

    conn.close()

    return data

def get_course_analysis():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            course,
            COUNT(*),
            AVG(marks)
        FROM students
        GROUP BY course
    """)

    data = cursor.fetchall()

    conn.close()

    return data
def get_top_students():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM students
        ORDER BY marks DESC
        LIMIT 5
    """)

    data = cursor.fetchall()

    conn.close()

    return data

