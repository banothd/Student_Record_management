# for User interface

import streamlit as st
from student import Student
from database import *

# Sidebar menu
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
    layout="wide"
)

st.title("Student Record Management System")

# Dashboard
if menu == "Dashboard":

    st.header("Analytics Dashboard")

    total = get_total_students()

    avg_marks, max_marks, min_marks = get_marks_statistics()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Students", total)
    col2.metric("Average Marks", round(avg_marks or 0, 2))
    col3.metric("Highest Marks", max_marks or 0)
    col4.metric("Lowest Marks", min_marks or 0)

    st.subheader("Course Analysis")

    courses = get_course_analysis()


    if courses:
        formatted_students = []

        for s in courses:
            formatted_students.append({
                "Course": s[0],
                "Total Students": s[1],
                "Average Marks": round(s[2] or 0, 2)
            })

        st.dataframe(formatted_students)

    else:
        st.info("No course records found.")

    st.subheader("Top 5 Students")

    top_students = get_top_students()

    if top_students:
        formatted_students = []

        for s in top_students:
            formatted_students.append({
                "ID": s[0],
                "Name": s[1],
                "Age": s[2],
                "Course": s[3],
                "Marks": s[4],
                "Grade": s[5]
            })

        st.dataframe(formatted_students)

    else:

        st.info("No student records found.")

# Add Student 
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

# View Students
elif menu == "View Students":

    st.header("Student Records")

    students = get_students()

    if students:

        formatted_students = []

        for s in students:
            formatted_students.append({
                "ID": s[0],
                "Name": s[1],
                "Age": s[2],
                "Course": s[3],
                "Marks": s[4],
                "Grade": s[5]
            })

        st.dataframe(formatted_students)

    else:
        st.info("No student records found.")

# Search Student
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

# Update Student
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

# Delete Student
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

