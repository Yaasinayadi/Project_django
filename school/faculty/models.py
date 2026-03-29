from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    head_teacher = models.ForeignKey(
        'Teacher', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='headed_department'
    )

    def __str__(self):
        return self.name


class Teacher(models.Model):
    teacher_id = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')])
    date_of_birth = models.DateField()
    mobile_number = models.CharField(max_length=20)
    joining_date = models.DateField()
    qualification = models.CharField(max_length=150)
    experience = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to='teachers/', blank=True, null=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='teachers'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.teacher_id})"


class Subject(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50, unique=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='subjects'
    )
    teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='subjects'
    )

    def __str__(self):
        return f"{self.name} ({self.code})"
