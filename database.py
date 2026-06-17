
# SQLite was chosen over CSV files because it provides better data integrity, faster querying, easier record management, and supports analytical operations efficiently

import sqlite3

DB_NAME = "students.db"

# Database functions for managing student records and analytics
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

#  add student record to the database
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

# fetch all student records from the database
def get_students():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT student_id, name, age, course, marks, grade
        FROM students
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows

# fetch a specific student record by ID
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

# update an existing student record in the database
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

# delete a student record from the database by ID
def delete_student(student_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE student_id = ?",
        (student_id,)
    )

    conn.commit()
    conn.close()

# analytics functions to provide insights into student performance and demographics
def get_total_students():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")

    total = cursor.fetchone()[0]

    conn.close()

    return total

# fetch average, maximum, and minimum marks from the database
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

# fetch course-wise student count and average marks from the database
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

# fetch top 5 students based on marks from the database
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

