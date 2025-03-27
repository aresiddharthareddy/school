from django import forms
from .models import Teacher, Student, Assignment, Scores


class LoginForm(forms.Form):
    name = forms.CharField(max_length=100, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    
    ROLE_CHOICES = [
        ("admin", "Superuser (Admin)"),
        ("teacher", "Teacher"),
        ("student", "Student"),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES, label="Login as")


class TeacherEditForm(forms.ModelForm):
    class Meta:
        model= Teacher
        fields = ['name', 'email', 'unique_id', 'subject', 'city', 'gender']

class TeacherForm(forms.ModelForm):
    # password = forms.PasswordInput()
    class Meta:
        model = Teacher
        fields = '__all__'
    
    password = forms.CharField(widget=forms.PasswordInput())

# class TeacherAssignmentForm(forms.ModelForm):
#     class Meta:
#         model = Teacher
#         fields = ['assignment_name','file_upload']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'city', 'gender', 'standard', 'password', 'roll_no' ]    
    
    password = forms.CharField(widget=forms.PasswordInput())

class StudentEditForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'city', 'gender', 'standard']    

class StudentSubjectForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['teachers']
        labels ={
            'teachers':'subject'
        }


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['teacher', 'assignment_name', 'file_upload']

class AssignmentSubmissionForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['file_upload']

class ScoresForm(forms.ModelForm):
    class Meta:
        model = Scores
        fields = ['student', 'assignment', 'file_upload']

class ScoresAddForm(forms.ModelForm):
    class Meta:
        model = Scores
        fields = ['student', 'scores', 'assignment']
        
class ScoresUpdateForm(forms.ModelForm):
    class Meta:
        model = Scores
        fields = ['scores']