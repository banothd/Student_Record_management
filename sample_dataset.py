from student import Student
from database import add_student

students = [
    Student(101, "Aarav Sharma", 20, "Python", 88),
    Student(102, "Priya Patel", 21, "Data Science", 92),
    Student(103, "Rahul Verma", 19, "Python", 76),
    Student(104, "Sneha Reddy", 22, "AI", 85),
    Student(105, "Arjun Kumar", 20, "Machine Learning", 95),
    Student(106, "Ananya Singh", 21, "Data Science", 68),
    Student(107, "Karan Mehta", 23, "Python", 81),
    Student(108, "Neha Gupta", 20, "AI", 73),
    Student(109, "Rohan Das", 22, "Machine Learning", 90),
    Student(110, "Meera Iyer", 19, "Python", 64),
    Student(111, "Vikram Joshi", 21, "Data Science", 87),
    Student(112, "Pooja Nair", 20, "AI", 78),
    Student(113, "Aditya Rao", 22, "Machine Learning", 59),
    Student(114, "Kavya Menon", 21, "Python", 97),
    Student(115, "Siddharth Jain", 20, "AI", 83),
    Student(116, "Divya Mishra", 23, "Data Science", 72),
    Student(117, "Nikhil Shah", 19, "Python", 66),
    Student(118, "Ishita Roy", 20, "Machine Learning", 89),
    Student(119, "Manish Yadav", 22, "AI", 54),
    Student(120, "Riya Chawla", 21, "Data Science", 91),
    Student(121, "Akash Bhat", 20, "Python", 79),
    Student(122, "Shreya Kulkarni", 22, "Machine Learning", 84),
    Student(123, "Harsh Agarwal", 19, "AI", 62),
    Student(124, "Tanvi Desai", 21, "Data Science", 94),
    Student(125, "Yash Malhotra", 20, "Python", 71)
]

for student in students:
    try:
        add_student(student)
    except Exception:
        pass

print("Sample data inserted successfully.")