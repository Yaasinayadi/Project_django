import os
import django
import random
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school.settings')
django.setup()

from faculty.models import Department, Subject, Teacher, Holiday, TimeTable, Exam, ExamResult
from student.models import Student, Parent

male_first_names = ["Youssef", "Karim", "Amine", "Mehdi", "Omar", "Hamza", "Ilyas", "Rachid", "Hassan", "Zakaria", "Ayman", "Yassine"]
female_first_names = ["Fatima", "Khadija", "Salma", "Majda", "Meryem", "Imane", "Hiba", "Zineb", "Kenza", "Nada", "Chaimae"]
last_names = ["ali", "Barak", "Settati", "Alami", "Kawtar", "Taji", "Mane", "El Samira", "Ben hmed", "Lamine", "Ahmadi"]
cities = ["Casablanca", "Rabat", "Fès", "Tanger", "Marrakech", "Agadir", "Oujda", "Tétouan"]
streets = ["Hassan 2", "Boulevard Mohammed V", "Rue Marjane", "Boukhalef", "Riad Ahlan", "Tanja balia"]

print('Suppression des anciennes données...')
ExamResult.objects.all().delete()
Exam.objects.all().delete()
TimeTable.objects.all().delete()
Holiday.objects.all().delete()
Subject.objects.all().delete()
Teacher.objects.all().delete()
Department.objects.all().delete()
Student.objects.all().delete()
Parent.objects.all().delete()

print('Création des départements...')
departments = []
for name in ['Mathématiques', 'Physique-Chimie', 'Informatique', 'Langues', 'SVT']:
    dept = Department.objects.create(name=name, description=f"Département de {name}")
    departments.append(dept)

print('Création des enseignants...')
teachers = []
for i in range(10):
    dept = random.choice(departments)
    gender = random.choice(["Male", "Female"])
    first_name = random.choice(male_first_names) if gender == "Male" else random.choice(female_first_names)
    last_name = random.choice(last_names)
    city = random.choice(cities)
    
    teacher = Teacher.objects.create(
        teacher_id=f"T{i+1000}",
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        date_of_birth=date(1975 + random.randint(0, 15), random.randint(1, 12), random.randint(1, 28)),
        mobile_number=f"06{random.randint(10000000, 99999999)}",
        joining_date=date(2018 + random.randint(0, 5), random.randint(1, 12), 1),
        qualification="Master / Doctorat",
        experience=f"{random.randint(2, 15)} Ans",
        username=f"{first_name.lower()}.{last_name.lower()}",
        email=f"{first_name.lower()}.{last_name.lower()}@preskool.ma",
        password="password123",
        address=f"{random.randint(1, 150)} {random.choice(streets)}",
        city=city,
        state=city,
        zip_code=f"{random.randint(10000, 90000)}",
        country="Maroc",
        department=dept
    )
    teachers.append(teacher)

for dept in departments:
    dept_teachers = [t for t in teachers if t.department == dept]
    
    if len(dept_teachers) > 0:
        dept.head_teacher = random.choice(dept_teachers)
        dept.save()


print('Création des matières...')
subjects = []
subject_names = ['Algèbre', 'Analyse', 'Physique', 'Chimie', 'SVT', 'Programmation Python', 'Développement Web', 'Arabe', 'Français', 'Anglais']
for idx, name in enumerate(subject_names):
    dept = random.choice(departments)
    dept_teachers = [t for t in teachers if t.department == dept]
    teacher = random.choice(dept_teachers) if dept_teachers else random.choice(teachers)
    
    sub = Subject.objects.create(name=name, code=f"SUBJ{idx+100}", department=dept, teacher=teacher)
    subjects.append(sub)

print('Création des étudiants et parents...')
students = []
for i in range(15):
    family_last_name = random.choice(last_names)
    father_fn = random.choice(male_first_names)
    mother_fn = random.choice(female_first_names)
    mother_ln = random.choice(last_names)
    
    address = f"{random.randint(1, 200)} {random.choice(streets)}, {random.choice(cities)}"
    
    parent = Parent.objects.create(
        father_name=f"{father_fn} {family_last_name}",
        father_occupation=random.choice(["Ingénieur", "Médecin", "Commerçant", "Fonctionnaire", "Professeur"]),
        father_mobile=f"06{random.randint(10000000, 99999999)}",
        father_email=f"{father_fn.lower()}.{family_last_name.lower()}@gmail.com",
        mother_name=f"{mother_fn} {mother_ln}",
        mother_occupation=random.choice(["Femme au foyer", "Avocate", "Enseignante", "Comptable"]),
        mother_mobile=f"06{random.randint(10000000, 99999999)}",
        mother_email=f"{mother_fn.lower()}.{mother_ln.lower()}@gmail.com",
        present_address=address,
        permanent_address=address
    )
    
    student_gender = random.choice(["Male", "Female"])
    student_fn = random.choice(male_first_names) if student_gender == "Male" else random.choice(female_first_names)
    
    student = Student.objects.create(
        first_name=student_fn,
        last_name=family_last_name,
        student_id=f"S{i+202400}",
        gender=student_gender,
        date_of_birth=date(2004 + random.randint(0, 3), random.randint(1, 12), random.randint(1, 28)),
        student_class=random.choice(["1ère Année Bac", "2ème Année Bac", "Tronc Commun"]),
        joining_date=date(2023, 9, 5),
        mobile_number=f"07{random.randint(10000000, 99999999)}",
        admission_number=f"A{i+5000}",
        section=random.choice(["A", "B", "C"]),
        parent=parent
    )
    students.append(student)

print('Création de l\'emploi du temps et examens...')
Holiday.objects.create(name="Vacances d'Été", type="Vacances", start_date=date(2026, 7, 10), end_date=date(2026, 9, 2))
Holiday.objects.create(name="Aïd Al Fitr", type="Jour Férié", start_date=date(2026, 3, 20), end_date=date(2026, 3, 23))

for i in range(12):
    sub = random.choice(subjects)
    TimeTable.objects.create(
        department=sub.department,
        subject=sub,
        teacher=sub.teacher,
        day_of_week=random.choice(['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']),
        start_time=random.choice(["08:30:00", "10:30:00", "14:30:00"]),
        end_time=random.choice(["10:15:00", "12:15:00", "16:15:00"])
    )

for i in range(6):
    sub = random.choice(subjects)
    exam = Exam.objects.create(
        name=f"Contrôle Continu {i+1} - {sub.name}",
        subject=sub,
        exam_date=date(2026, 11, random.randint(1, 28)),
        start_time="08:30:00",
        end_time="10:30:00",
        total_marks=20
    )
    for j in range(4):
        ExamResult.objects.create(
            exam=exam,
            student=random.choice(students),
            marks_obtained=random.randint(8, 20),
            comments=random.choice(["Excellent", "Bon travail", "Peut mieux faire", "Assez bien"])
        )

# Update the welcome message to include the username dynamically
print(f"✅ Base de données initialisée avec succès pour {os.getenv('USER', 'utilisateur inconnu')} !")