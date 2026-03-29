from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Teacher
from django.contrib import messages 

def index(request):
    return render(request, 'authentication/login.html')

def dashboard(request):
    return render(request, 'students/student-dashboard.html')

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/teachers.html', {'teachers': teachers})

def add_teacher(request):
    if request.method == 'POST':
        teacher_id = request.POST.get('teacher_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        mobile_number = request.POST.get('mobile_number')
        joining_date = request.POST.get('joining_date')
        qualification = request.POST.get('qualification')
        experience = request.POST.get('experience')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        country = request.POST.get('country')
        image = request.FILES.get('image')

        teacher = Teacher.objects.create(
            teacher_id=teacher_id,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            date_of_birth=date_of_birth,
            mobile_number=mobile_number,
            joining_date=joining_date,
            qualification=qualification,
            experience=experience,
            username=username,
            email=email,
            password=password,
            address=address,
            city=city,
            state=state,
            zip_code=zip_code,
            country=country,
            image=image
        )
        messages.success(request, 'Teacher added successfully')
        return redirect('teacher_list')
    return render(request, 'teachers/add-teacher.html')

def edit_teacher(request, teacher_id):
    teacher = Teacher.objects.get(teacher_id=teacher_id)
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
        teacher.save()
        messages.success(request, 'Teacher updated successfully')
        return redirect('teacher_list')
    return render(request, 'teachers/edit-teacher.html', {'teacher': teacher})

def view_teacher(request, teacher_id):
    teacher = Teacher.objects.get(teacher_id=teacher_id)
    return render(request, 'teachers/teacher-details.html', {'teacher': teacher})

def delete_teacher(request, teacher_id):
    teacher = Teacher.objects.get(teacher_id=teacher_id)
    teacher.delete()
    messages.success(request, 'Teacher deleted successfully')
    return redirect('teacher_list')