from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User



#Abstract Base Model (Common Fields)
class Common(models.Model):
    GENDER_CHOICES=[
        ('M', 'male'),
        ('F', 'female'),
        ('O', 'others')
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    gender= models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    password = models.CharField(max_length=128)
    city=models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True  # This prevents creating a separate table
    

    def save(self, *args, **kwargs):
        """ Hash password only if it's not already hashed """
        if not self.password.startswith('pbkdf2_sha256$'):  # Check if password is already hashed
            self.password = make_password(self.password)  
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        """ Check if a raw password matches the hashed password """
        return check_password(raw_password, self.password)


class Teacher(Common):
    unique_id = models.CharField(max_length=50, unique=True)
    subject = models.CharField(max_length=100)
    assignment_name= models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"(Subject: {self.subject})"

#Student Model
class Student(Common):
    roll_no = models.IntegerField(unique=True)
    standard= models.IntegerField()
    teachers = models.ManyToManyField(Teacher, related_name="students")

    def __str__(self):
        return f"Student: {self.name} (Roll No: {self.roll_no})"

#Assignment Model
class Assignment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="assignments")  
    assignment_name = models.TextField()
    file_upload= models.FileField(upload_to= 'assignments_submitted/', null = True, blank=True)

    def __str__(self):
        return f"Assignment: {self.assignment_name} (Teacher: {self.teacher.name})"

    
class Scores(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE, related_name="Scores", null=True, blank=True)
    assignment=models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="Scores", null=True, blank=True)
    scores=models.IntegerField(null= True, blank=True)
    file_upload= models.FileField(upload_to= 'students_assignment/', null = True, blank=True)


