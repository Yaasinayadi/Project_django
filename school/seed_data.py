import os
import django
import random
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school.settings')
django.setup()

from faculty.models import Department, Subject, Teacher, Holiday, TimeTable, Exam, ExamResult
from student.models import Student, Parent

# Clear existing data
print('Clearing existing data...')
ExamResult.objects.all().delete()
Exam.objects.all().delete()
TimeTable.objects.all().delete()
Holiday.objects.all().delete()
Subject.objects.all().delete()
Teacher.objects.all().delete()
Department.objects.all().delete()
Student.objects.all().delete()
Parent.objects.all().delete()

# Create Departments
departments = []
for name in ['Mathematics', 'Science', 'Computer Science', 'Languages']:
    dept = Department.objects.create(name=name, description=f"{name} Department")
    departments.append(dept)

# Create Teachers
teachers = []
for i in range(15):
    dept = random.choice(departments)
    teacher = Teacher.objects.create(
        teacher_id=f"T{i+1000}",
        first_name=f"ProfName{i}",
        last_name=f"ProfLastName{i}",
        gender=random.choice(["Male", "Female"]),
        date_of_birth=date(1980 + (i % 10), 1, 1),
        mobile_number=f"06000000{i:02d}",
        joining_date=date(2021, 1, 1),
        qualification="Master's Degree",
        experience=f"{i%5+2} Years",
        username=f"teacher{i}",
        email=f"teacher{i}@school.com",
        password="password123",
        address="123 Teacher St",
        city="Paris",
        state="IDF",
        zip_code="75000",
        country="France",
        department=dept
    )
    teachers.append(teacher)

# Assign a head teacher to each department
for dept in departments:
    head = random.choice([t for t in teachers if t.department == dept]) if teachers else None
    if head:
        dept.head_teacher = head
        dept.save()

# Create Subjects
subjects = []
subject_names = ['Algebra', 'Physics', 'Biology', 'Python Programming', 'English', 'French']
for idx, name in enumerate(subject_names):
    dept = random.choice(departments)
    teacher = random.choice([t for t in teachers if t.department == dept]) if [t for t in teachers if t.department == dept] else random.choice(teachers)
    sub = Subject.objects.create(name=name, code=f"SUBJ{idx+100}", department=dept, teacher=teacher)
    subjects.append(sub)

# Create Students & Parents
students = []
for i in range(30):
    parent = Parent.objects.create(
        father_name=f"Papa {i}",
        father_occupation="Engineer",
        father_mobile=f"06123456{i:02d}",
        father_email=f"papa{i}@test.com",
        mother_name=f"Mama {i}",
        mother_occupation="Teacher",
        mother_mobile=f"06234567{i:02d}",
        mother_email=f"mama{i}@test.com",
        present_address=f"123 Street {i}",
        permanent_address=f"123 Street {i}"
    )
    student = Student.objects.create(
        first_name=f"Student{i}",
        last_name=f"LastName{i}",
        student_id=f"S{i+2000}",
        gender=random.choice(["Male", "Female"]),
        date_of_birth=date(2005 + random.randint(0, 3), random.randint(1, 12), random.randint(1, 28)),
        student_class=f"Class {random.randint(9, 12)}",
        joining_date=date(2022, 9, 1),
        mobile_number=f"07000000{i:02d}",
        admission_number=f"A{i+5000}",
        section=random.choice(["A", "B", "C"]),
        parent=parent
    )
    students.append(student)

# Create Holidays
Holiday.objects.create(name="Summer Vacation", type="Vacation", start_date=date(2026, 7, 1), end_date=date(2026, 8, 31))
Holiday.objects.create(name="Winter Vacation", type="Vacation", start_date=date(2026, 12, 20), end_date=date(2027, 1, 5))

# Create TimeTables
for i in range(10):
    sub = random.choice(subjects)
    TimeTable.objects.create(
        department=sub.department,
        subject=sub,
        teacher=sub.teacher,
        day_of_week=random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']),
        start_time="09:00:00",
        end_time="10:30:00"
    )

# Create Exams and Results
for i in range(5):
    sub = random.choice(subjects)
    exam = Exam.objects.create(
        name=f"Midterm Exam {i+1}",
        subject=sub,
        exam_date=date(2026, 11, 15) + timedelta(days=i),
        start_time="14:00:00",
        end_time="16:00:00",
        total_marks=100
    )
    for j in range(5):  # 5 results per exam
        ExamResult.objects.create(
            exam=exam,
            student=random.choice(students),
            marks_obtained=random.randint(40, 100),
            comments="Good"
        )

print("Database thoroughly seeded with 30 students, 15 teachers, and hundreds of relations successfully!")
