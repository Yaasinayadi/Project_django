from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher, Department, Subject, Holiday, TimeTable, Exam, ExamResult
from student.models import Student
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'authentication/login.html')

@login_required
def dashboard(request):
    if request.user.is_admin:
        return render(request, 'Home/index.html') 
    elif request.user.is_teacher:
        return render(request, 'teachers/teacher-dashboard.html')
    elif request.user.is_student:
        return render(request, 'students/student-dashboard.html')
    else:
        return redirect('login') 

def admin_dashboard(request):
    return render(request, 'Home/index.html')


def teacher_dashboard(request):
    return render(request, 'teachers/teacher-dashboard.html')


@login_required
def teacher_list(request):
    if not request.user.is_admin:
        messages.error(request, "Accès non autorisé.")
        return redirect('dashboard')
    teachers = Teacher.objects.all()
    return render(request, 'teachers/teachers.html', {'teachers': teachers})

@login_required
def add_teacher(request):
    if not request.user.is_admin:
        messages.error(request, "Accès non autorisé.")
        return redirect('dashboard')
    departments = Department.objects.all()
    if request.method == 'POST':
        department_id = request.POST.get('department')
        department = None
        if department_id:
            department = get_object_or_404(Department, pk=department_id)

        teacher = Teacher.objects.create(
            teacher_id=request.POST.get('teacher_id'),
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            gender=request.POST.get('gender'),
            date_of_birth=request.POST.get('date_of_birth'),
            mobile_number=request.POST.get('mobile_number'),
            joining_date=request.POST.get('joining_date'),
            qualification=request.POST.get('qualification'),
            experience=request.POST.get('experience'),
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            password=request.POST.get('password'),
            address=request.POST.get('address'),
            city=request.POST.get('city'),
            state=request.POST.get('state'),
            zip_code=request.POST.get('zip_code'),
            country=request.POST.get('country'),
            image=request.FILES.get('image'),
            department=department,
        )
        messages.success(request, 'Teacher added successfully')
        return redirect('teacher_list')
    return render(request, 'teachers/add-teacher.html', {'departments': departments})

@login_required
def edit_teacher(request, teacher_id):
    if not request.user.is_admin:
        messages.error(request, "Accès non autorisé.")
        return redirect('dashboard')
    teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
    departments = Department.objects.all()
    if request.method == 'POST':
        teacher.first_name = request.POST.get('first_name')
        teacher.last_name = request.POST.get('last_name')
        teacher.gender = request.POST.get('gender')
        teacher.date_of_birth = request.POST.get('date_of_birth')
        teacher.mobile_number = request.POST.get('mobile_number')
        teacher.joining_date = request.POST.get('joining_date')
        teacher.qualification = request.POST.get('qualification')
        teacher.experience = request.POST.get('experience')
        teacher.username = request.POST.get('username')
        teacher.email = request.POST.get('email')
        if request.POST.get('password'):
            teacher.password = request.POST.get('password')
        teacher.address = request.POST.get('address')
        teacher.city = request.POST.get('city')
        teacher.state = request.POST.get('state')
        teacher.zip_code = request.POST.get('zip_code')
        teacher.country = request.POST.get('country')
        if request.FILES.get('image'):
            teacher.image = request.FILES.get('image')

        department_id = request.POST.get('department')
        if department_id:
            teacher.department = get_object_or_404(Department, pk=department_id)
        else:
            teacher.department = None

        teacher.save()
        messages.success(request, 'Teacher updated successfully')
        return redirect('teacher_list')
    return render(request, 'teachers/edit-teacher.html', {'teacher': teacher, 'departments': departments})

@login_required
def view_teacher(request, teacher_id):
    if not request.user.is_admin:
        messages.error(request, "Accès non autorisé.")
        return redirect('dashboard')
    teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
    return render(request, 'teachers/teacher-details.html', {'teacher': teacher})


@login_required
def delete_teacher(request, teacher_id):
    if not request.user.is_admin:
        messages.error(request, "Accès non autorisé.")
        return redirect('dashboard')
    teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
    teacher.delete()
    messages.success(request, 'Teacher deleted successfully')
    return redirect('teacher_list')

@login_required
def department_list(request):
    if not request.user.is_admin:
        messages.error(request, "Accès non autorisé.")
        return redirect('dashboard')
    departments = Department.objects.all()
    return render(request, 'departments/departments.html', {'departments': departments})

@login_required
def add_department(request):
    if not request.user.is_admin:
        messages.error(request, "Accès non autorisé.")
        return redirect('dashboard')
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        head_teacher_id = request.POST.get('head_teacher')
        head_teacher = None
        if head_teacher_id:
            head_teacher = get_object_or_404(Teacher, pk=head_teacher_id)

        Department.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            head_teacher=head_teacher,
        )
        messages.success(request, 'Department added successfully')
        return redirect('department_list')
    return render(request, 'departments/add-department.html', {'teachers': teachers})

@login_required
def edit_department(request, pk):
    if not request.user.is_admin:
        messages.error(request, "Accès non autorisé.")
        return redirect('dashboard')
    department = get_object_or_404(Department, pk=pk)
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        department.name = request.POST.get('name')
        department.description = request.POST.get('description')

        head_teacher_id = request.POST.get('head_teacher')
        if head_teacher_id:
            department.head_teacher = get_object_or_404(Teacher, pk=head_teacher_id)
        else:
            department.head_teacher = None

        department.save()
        messages.success(request, 'Department updated successfully')
        return redirect('department_list')
    return render(request, 'departments/edit-department.html', {'department': department, 'teachers': teachers})

def view_department(request, pk):
    
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'departments/department-details.html', {'department': department})


@login_required
def delete_department(request, pk):
    if not request.user.is_admin:
        messages.error(request, "Accès non autorisé.")
        return redirect('dashboard')
    department = get_object_or_404(Department, pk=pk)
    department.delete()
    messages.success(request, 'Department deleted successfully')
    return redirect('department_list')

@login_required
def subject_list(request):
    if request.user.is_student:
        messages.error(request, "Accès non autorisé.")
        return redirect('dashboard')
    subjects = Subject.objects.all()
    return render(request, 'subjects/subjects.html', {'subjects': subjects})

@login_required
def add_subject(request):
    if not request.user.is_admin:
        messages.error(request, "Accès non autorisé.")
        return redirect('dashboard')
    departments = Department.objects.all()
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        department_id = request.POST.get('department')
        teacher_id = request.POST.get('teacher')
        department = None
        teacher = None
        if department_id:
            department = get_object_or_404(Department, pk=department_id)
        if teacher_id:
            teacher = get_object_or_404(Teacher, pk=teacher_id)

        Subject.objects.create(
            name=request.POST.get('name'),
            code=request.POST.get('code'),
            department=department,
            teacher=teacher,
        )
        messages.success(request, 'Subject added successfully')
        return redirect('subject_list')
    return render(request, 'subjects/add-subject.html', {'departments': departments, 'teachers': teachers})

@login_required
def edit_subject(request, pk):
    if not request.user.is_admin:
        messages.error(request, "Accès non autorisé.")
        return redirect('dashboard')
    subject = get_object_or_404(Subject, pk=pk)
    departments = Department.objects.all()
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        subject.name = request.POST.get('name')
        subject.code = request.POST.get('code')

        department_id = request.POST.get('department')
        if department_id:
            subject.department = get_object_or_404(Department, pk=department_id)
        else:
            subject.department = None

        teacher_id = request.POST.get('teacher')
        if teacher_id:
            subject.teacher = get_object_or_404(Teacher, pk=teacher_id)
        else:
            subject.teacher = None

        subject.save()
        messages.success(request, 'Subject updated successfully')
        return redirect('subject_list')
    return render(request, 'subjects/edit-subject.html', {'subject': subject, 'departments': departments, 'teachers': teachers})


def view_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    return render(request, 'subjects/subject-details.html', {'subject': subject})

@login_required
def delete_subject(request, pk):
    if not request.user.is_admin:
        messages.error(request, "Accès non autorisé.")
        return redirect('dashboard')
    subject = get_object_or_404(Subject, pk=pk)
    subject.delete()
    messages.success(request, 'Subject deleted successfully')
    return redirect('subject_list')


@login_required
def holiday_list(request):
    if not request.user.is_admin:
        messages.error(request, "Accès non autorisé.")
        return redirect('dashboard')
    holidays = Holiday.objects.all()
    return render(request, 'holidays/holidays.html', {'holidays': holidays})


@login_required
def add_holiday(request):
    if not request.user.is_admin:
        messages.error(request, "Accès non autorisé.")
        return redirect('dashboard')
    if request.method == 'POST':
        Holiday.objects.create(
            name=request.POST.get('name'),
            type=request.POST.get('type'),
            start_date=request.POST.get('start_date'),
            end_date=request.POST.get('end_date'),
        )
        messages.success(request, 'Holiday added successfully')
        return redirect('holiday_list')
    return render(request, 'holidays/add-holiday.html')


@login_required
def edit_holiday(request, pk):
    if not request.user.is_admin:
        messages.error(request, "Accès non autorisé.")
        return redirect('dashboard')
    holiday = get_object_or_404(Holiday, pk=pk)
    if request.method == 'POST':
        holiday.name = request.POST.get('name')
        holiday.type = request.POST.get('type')
        holiday.start_date = request.POST.get('start_date')
        holiday.end_date = request.POST.get('end_date')
        holiday.save()
        messages.success(request, 'Holiday updated successfully')
        return redirect('holiday_list')
    return render(request, 'holidays/edit-holiday.html', {'holiday': holiday})


@login_required
def delete_holiday(request, pk):
    if not request.user.is_admin:
        messages.error(request, "Accès non autorisé.")
        return redirect('dashboard')
    holiday = get_object_or_404(Holiday, pk=pk)
    holiday.delete()
    messages.success(request, 'Holiday deleted successfully')
    return redirect('holiday_list')

@login_required
def time_table_list(request):
    if not request.user.is_admin:
        messages.error(request, "Accès non autorisé.")
        return redirect('dashboard')
    time_tables = TimeTable.objects.all().order_by('day_of_week', 'start_time')
    return render(request, 'timetable/time-table.html', {'time_tables': time_tables})

@login_required
def add_time_table(request):
    if not request.user.is_admin:
        messages.error(request, "Accès non autorisé.")
        return redirect('dashboard')
    departments = Department.objects.all()
    subjects = Subject.objects.all()
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        TimeTable.objects.create(
            department_id=request.POST.get('department'),
            subject_id=request.POST.get('subject'),
            teacher_id=request.POST.get('teacher'),
            day_of_week=request.POST.get('day_of_week'),
            start_time=request.POST.get('start_time'),
            end_time=request.POST.get('end_time'),
        )
        messages.success(request, 'Time Table entry added successfully')
        return redirect('time_table_list')
    return render(request, 'timetable/add-time-table.html', {
        'departments': departments,
        'subjects': subjects,
        'teachers': teachers
    })

@login_required
def edit_time_table(request, pk):
    if not request.user.is_admin:
        messages.error(request, "Accès non autorisé.")
        return redirect('dashboard')
    time_table = get_object_or_404(TimeTable, pk=pk)
    departments = Department.objects.all()
    subjects = Subject.objects.all()
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        time_table.department_id = request.POST.get('department')
        time_table.subject_id = request.POST.get('subject')
        time_table.teacher_id = request.POST.get('teacher')
        time_table.day_of_week = request.POST.get('day_of_week')
        time_table.start_time = request.POST.get('start_time')
        time_table.end_time = request.POST.get('end_time')
        time_table.save()
        messages.success(request, 'Time Table entry updated successfully')
        return redirect('time_table_list')
    return render(request, 'timetable/edit-time-table.html', {
        'time_table': time_table,
        'departments': departments,
        'subjects': subjects,
        'teachers': teachers
    })

@login_required
def delete_time_table(request, pk):
    if not request.user.is_admin:
        messages.error(request, "Accès non autorisé.")
        return redirect('dashboard')
    time_table = get_object_or_404(TimeTable, pk=pk)
    time_table.delete()
    messages.success(request, 'Time Table entry deleted successfully')
    return redirect('time_table_list')

def exam_list(request):
    exams = Exam.objects.all().order_by('-exam_date')
    return render(request, 'exams/exams.html', {'exams': exams})

@login_required
def add_exam(request):
    if not request.user.is_admin:
        messages.error(request, "Accès non autorisé.")
        return redirect('dashboard')
    subjects = Subject.objects.all()
    if request.method == 'POST':
        Exam.objects.create(
            name=request.POST.get('name'),
            subject_id=request.POST.get('subject'),
            exam_date=request.POST.get('exam_date'),
            start_time=request.POST.get('start_time'),
            end_time=request.POST.get('end_time'),
            total_marks=request.POST.get('total_marks'),
        )
        messages.success(request, 'Exam scheduled successfully')
        return redirect('exam_list')
    return render(request, 'exams/add-exam.html', {'subjects': subjects})

@login_required
def edit_exam(request, pk):
    if not request.user.is_admin:
        messages.error(request, "Accès non autorisé.")
        return redirect('dashboard')
    exam = get_object_or_404(Exam, pk=pk)
    subjects = Subject.objects.all()
    if request.method == 'POST':
        exam.name = request.POST.get('name')
        exam.subject_id = request.POST.get('subject')
        exam.exam_date = request.POST.get('exam_date')
        exam.start_time = request.POST.get('start_time')
        exam.end_time = request.POST.get('end_time')
        exam.total_marks = request.POST.get('total_marks')
        exam.save()
        messages.success(request, 'Exam updated successfully')
        return redirect('exam_list')
    return render(request, 'exams/edit-exam.html', {'exam': exam, 'subjects': subjects})

def delete_exam(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    exam.delete()
    messages.success(request, 'Exam deleted successfully')
    return redirect('exam_list')

def exam_results(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    students = Student.objects.all()
    
    if request.method == 'POST':
        # the form will submit a dictionary of student IDs to their marks
        student_id = request.POST.get('student_id')
        marks = request.POST.get('marks_obtained')
        comments = request.POST.get('comments', '')
        
        if student_id and marks:
            student = get_object_or_404(Student, student_id=student_id)
            result, created = ExamResult.objects.get_or_create(
                exam=exam, student=student,
                defaults={'marks_obtained': marks, 'comments': comments}
            )
            if not created:
                result.marks_obtained = marks
                result.comments = comments
                result.save()
            messages.success(request, f'Result updated for {student.first_name}')
            return redirect('exam_results', pk=exam.pk)

    results = ExamResult.objects.filter(exam=exam).select_related('student')
    
    # create a dictionary of existing results for the template
    results_dict = {str(res.student.student_id): res for res in results}
    
    context = {
        'exam': exam,
        'students': students,
        'results_dict': results_dict
    }
    return render(request, 'exams/exam-results.html', context)
