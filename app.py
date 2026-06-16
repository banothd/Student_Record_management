import streamlit as st

from student import Student

from database import (
    add_student,
    get_students,
    search_student,
    update_student,
    delete_student,
    get_total_students,
    get_marks_statistics,
    get_grade_distribution,
    get_course_analysis,
    get_top_students
)

menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Dashboard",
        "Add Student",
        "View Students",
        "Search Student",
        "Update Student",
        "Delete Student"
    ]
)

st.set_page_config(
    page_title="Student Record Management System",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Record Management System")


if menu == "Dashboard":

    st.header("📊 Analytics Dashboard")

    total = get_total_students()

    avg_marks, max_marks, min_marks = get_marks_statistics()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Students", total)
    col2.metric("Average Marks", round(avg_marks or 0, 2))
    col3.metric("Highest Marks", max_marks or 0)
    col4.metric("Lowest Marks", min_marks or 0)

    st.subheader("Grade Distribution")

    grades = get_grade_distribution()

    if grades:

        grade_data = {
            grade: count for grade, count in grades
        }

        st.bar_chart(grade_data)

    st.subheader("Course Analysis")

    courses = get_course_analysis()

    if courses:

        st.table(
            courses
        )

    st.subheader("🏆 Top Performers")

    top_students = get_top_students()

    if top_students:

        st.table(top_students)

    else:

        st.info("No student records found.")


elif menu == "Add Student":

    st.header("Add New Student")

    student_id = st.number_input(
        "Student ID",
        min_value=1,
        step=1
    )

    name = st.text_input("Student Name")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        step=1
    )

    course = st.text_input("Course")

    marks = st.number_input(
        "Marks",
        min_value=0.0,
        max_value=100.0
    )

    if st.button("Add Student"):

        student = Student(
            student_id,
            name,
            age,
            course,
            marks
        )

        try:

            add_student(student)

            st.success("Student added successfully.")

        except Exception as e:

            st.error(f"Error: {e}")


elif menu == "View Students":

    st.header("Student Records")

    students = get_students()

    if students:

        st.table(students)

    else:

        st.info("No student records found.")


elif menu == "Search Student":

    st.header("Search Student")

    student_id = st.number_input(
        "Enter Student ID",
        min_value=1,
        step=1
    )

    if st.button("Search"):

        student = search_student(student_id)

        if student:

            st.write(f"ID: {student[0]}")
            st.write(f"Name: {student[1]}")
            st.write(f"Age: {student[2]}")
            st.write(f"Course: {student[3]}")
            st.write(f"Marks: {student[4]}")
            st.write(f"Grade: {student[5]}")

        else:

            st.error("Student not found.")


elif menu == "Update Student":

    st.header("Update Student")

    student_id = st.number_input(
        "Roll Number",
        min_value=1,
        step=1
    )

    name = st.text_input("Student Name")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        step=1
    )

    course = st.text_input("Course")

    marks = st.number_input(
        "Marks",
        min_value=0.0,
        max_value=100.0
    )

    if st.button("Update Student"):

        student = Student(
            student_id,
            name,
            age,
            course,
            marks
        )

        try:
            update_student(student)
            st.success("Student updated successfully.")

        except Exception as e:
            st.error(f"Error: {e}")


elif menu == "Delete Student":

    st.header("Delete Student")

    student_id = st.number_input(
        "Enter Student ID",
        min_value=1,
        step=1
    )

    if st.button("Delete Student"):

        delete_student(student_id)

        st.success("Student deleted successfully.")

