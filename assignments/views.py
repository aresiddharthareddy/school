from django.shortcuts import render, redirect
from django.http import FileResponse
from django.views import View
from .models import Teacher, Student, Assignment, Scores
from .forms import TeacherForm, StudentForm, AssignmentForm, ScoresForm,ScoresAddForm, ScoresUpdateForm,TeacherEditForm, StudentEditForm, AssignmentSubmissionForm, LoginForm, StudentSubjectForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test


# ------------------ login Views ------------------
def is_superuser(user):
    return user.is_superuser

def login_user(request):
    if request.method == "POST":
        name = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")  # Get role (admin, teacher, student)

        if role == "admin":  # Superuser authentication
            user = authenticate(request, username=name, password=password)
            if user is not None and user.is_superuser:
                request.session["user_id"] = user.id
                request.session["username"] = user.username
                request.session["role"] = "admin"
                return redirect("admin_dashboard")
            else:
                messages.error(request, "Invalid admin username or password.")
                return redirect("login")
 
        elif role == "teacher":
            try:
                user = Teacher.objects.get(name=name)  # Check if teacher exists
            except Teacher.DoesNotExist:
                messages.error(request, "Invalid username or password for teacher.")
                return redirect("login")

        else:  # Student login
            try:
                user = Student.objects.get(name=name)  # Check if student exists
            except Student.DoesNotExist:
                messages.error(request, "Invalid username or password for student.")
                return redirect("login")

        # Verify password
        if check_password(password, user.password):
            request.session["user_id"] = user.id
            request.session["username"] = user.name
            request.session["role"] = role  # Either "teacher" or "student"

            # Debugging print statements
            print(f"User Logged In: {user.name}, ID: {user.id}, Role: {role}")
            print("Session Data:", request.session.items())  # Print session data

            if role == "teacher":
                request.session["teacher_id"] = user.id
                print(f"Teacher ID stored in session: {request.session.get('teacher_id')}")
                return redirect("teacher_list")
            else:
                request.session["student_id"] = user.id
                print(f"Student ID stored in session: {request.session.get('student_id')}")
                return redirect("student_list")  
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")

    return render(request, "login.html")  

@login_required
@user_passes_test(is_superuser)
def admin_dashboard(request):
    return render(request, "admin_dashboard.html")

def logout_user(request):
    request.session.flush()
    return redirect("login")

def logout_teacher(request):
    request.session.flush()
    return redirect("login")

def logout_student(request):
    request.session.flush()
    return redirect("login")




# ------------------ Teacher Views ------------------
class TeacherListView(View):
    def get(self, request):
        try:
            teachers = Teacher.objects.all()  # Fetch all teachers
            teacher_id = request.session.get("teacher_id")  # Retrieve logged-in teacher ID
            print("Logged-in teacher ID:", teacher_id)
            return render(request, "teacher_list.html", {"teachers": teachers, "teacher_id": teacher_id})
        except Teacher.DoesNotExist:
            return render(request, { "error_message": "Error retrieving teacher data." }, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured "}, 'error.html')

class TeacherCreateView(View):
    def get(self, request):
        try:
            form = TeacherForm()
            return render(request, 'teacher_form.html', {'form': form})
        except Teacher.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')

    def post(self, request):
        try:
            form = TeacherForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('teacher_list')
            return render(request, 'teacher_form.html', {'form': form})
        except Teacher.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')

class TeacherUpdateView(View):
    def get(self, request, id):
        try:
            teacher = Teacher.objects.get(id=id)
            form = TeacherEditForm(instance=teacher)
            return render(request, 'teacher_form.html', {'form': form})
        except Teacher.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')

    def post(self, request, id):
        try:
            teacher = Teacher.objects.get(id=id)
            form = TeacherEditForm(request.POST, request.FILES, instance=teacher)
            if form.is_valid():
                form.save()
                return redirect('teacher_list')
            return render(request, 'teacher_form.html', {'form': form})
        except Teacher.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')
    

class TeacherDeleteView(View):
    def get(self, request, id):
        try:
            teacher = Teacher.objects.get(id=id)
            return render(request, 'teacher_confirm_delete.html', {'teacher': teacher})
        except Teacher.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')

    def post(self, request, id):
        try:
            teacher = Teacher.objects.get(id=id)
            teacher.delete()
            return redirect('teacher_list')
        except Teacher.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')
    

class StudentListView(View):
    def get(self, request):
        try:
            students = Student.objects.all()
            student_id = request.session.get("student_id")  
            print("Logged-in student ID:", student_id) 
            return render(request, 'student_list.html', {'students': students , "student_id": student_id})
        except Student.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')

class StudentCreateView(View):
    def get(self, request):
        try:
            form = StudentForm()
            return render(request, 'student_form.html', {'form': form})
        except Student.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')


    def post(self, request):
        try:
            form = StudentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('student_list')
            return render(request, 'student_form.html', {'form': form})
        except Student.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')
    

class StudentUpdateView(View):
    def get(self, request, id):
        try:
            student = Student.objects.get(id=id)
            form = StudentEditForm(instance=student)
            return render(request, 'student_form.html', {'form': form})
        except Student.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')

    def post(self, request, id):
        try:
            student = Student.objects.get(id=id)
            form = StudentEditForm(request.POST, request.FILES, instance=student)
            if form.is_valid():
                form.save()
                return redirect('student_list')
            return render(request, 'student_form.html', {'form': form})
        except Student.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')

class StudentSubjectView(View):
    def get(self, request, id):
        try:
            student = Student.objects.get(id=id)
            form = StudentSubjectForm(instance=student)
            return render(request, 'student_form.html', {'form': form})
        except Student.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')

    def post(self, request, id):
        try:
            student = Student.objects.get(id=id)
            form = StudentSubjectForm(request.POST, instance=student)
            if form.is_valid():
                form.save()
                return redirect('student_list')
            return render(request, 'student_form.html', {'form':form})
        except Student.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')

class StudentDeleteView(View):
    def get(self, request, id):
        try:
            student= Student.objects.get(id=id)
            return render(request, 'student_confirm_delete.html', {'students': student})
        except Student.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')
    
    def post(self, request, id):
        try:
            student= Student.objects.get(id=id)
            student.delete()
            return redirect('student_list')
        except Student.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')



class AssignmentListView(View):
    def get(self, request, id=None):
        try:
            role = request.GET.get('role')
            # print("role:" ,role)
            if role == "teacher":
                assignments = Assignment.objects.filter(teacher=request.session.get("teacher_id"))
                
            else:
                assignments = Assignment.objects.all()
                
            return render(request, 'assignment_list.html', {'assignments': assignments, 'role': role })
        except Assignment.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')

class AssignmentCreateView(View):
    def get(self, request):
        try:
            form = AssignmentForm()
            return render(request, 'assignments_form.html', {'form': form})
        except Assignment.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')

    def post(self, request):
        try:
            form = AssignmentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('assignment_list')
            return render(request, 'assignments_form.html', {'form': form})
        except Assignment.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')

class AssignmentUpdateView(View):
    def get(self, request, id):
        try:
            assignment = Assignment.objects.get(id=id)
            form = AssignmentForm(instance=assignment)
            return render(request, 'assignments_form.html', {'form': form})
        except Assignment.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')

    def post(self, request, id):
        try:
            assignment = Assignment.objects.get(id=id)
            form = AssignmentSubmissionForm(request.POST, request.FILES, instance=assignment)
            if form.is_valid():
                form.save()
                return redirect('assignment_list')
            return render(request, 'assignments_form.html', {'form': form})
        except Assignment.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')

class AssignmentDeleteView(View):
    def get(self, request, id):
        try:
            assignment = Assignment.objects.get(id=id)
            return render(request, 'assignment_confirm_delete.html', {'assignment': assignment})
        except Assignment.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')

    def post(self, request, id):
        try:
            assignment = Assignment.objects.get(id=id)
            assignment.delete()
            return redirect('assignment_list')
        except Assignment.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')
    
class AssignmentSubmitView(View):
    def get(self, request, id):
        try:
            assignment = get_object_or_404(Assignment, id=id)
            form = AssignmentSubmissionForm()
            return render(request, 'assignment_submit.html', {'form': form, 'assignment': assignment})
        except Exception as e:
            return render(request, 'error.html', {"error_message": "Unexpected error occurred"})

    def post(self, request, id):
        try:
            assignment = get_object_or_404(Assignment, id=id)
            
            # No `instance=assignment` as this is a new submission, not an update
            form = AssignmentSubmissionForm(request.POST, request.FILES)  
            
            if form.is_valid():
                submission = form.save(commit=False)  # Delay saving to add more data
                submission.assignment = assignment  # Associate with the correct assignment
                submission.save()
                return redirect('assignment_list')
                
            return render(request, 'assignment_submit.html', {'form': form, 'assignment': assignment})
        except Exception as e:
            return render(request, 'error.html', {"error_message": "Unexpected error occurred"})


class AssignmentFileView(View):
    def get(self, request, pk):
        # Correct model reference
        assignment = get_object_or_404(Assignment, pk=pk)

        # Ensure file exists
        if not assignment.file_upload:
            return HttpResponse("No file found for this assignment.", content_type="text/plain")

        # Return file response for download or opening in browser
        try:
            file_path = assignment.file_upload.path
            return FileResponse(open(file_path, 'rb'), as_attachment=False)  # `as_attachment=True` for download
        except FileNotFoundError:
            raise Http404("File not found.")
        except Exception as e:
            return HttpResponse(f"Error opening file: {str(e)}", content_type="text/plain")
        
        
        
class ScoresListView(View):
    def get(self, request):
        role = request.GET.get('role')

        if role == "teacher":
            # Get the logged-in teacher's assignments and their scores
            scores = Scores.objects.filter(assignment__teacher=request.session.get("teacher_id"))
        
        elif role == "student":
            
            scores = Scores.objects.filter(student=request.session.get("student_id"))
        
        else:
            # If not a teacher, show all scores (for admins or students)
            scores = Scores.objects.all()

        return render(request, 'scores_list.html', {'scores': scores, 'role': role})


class ScoresCreateView(View):
    def get(self, request):
        # try:
        form = ScoresForm()
        return render(request, 'scores_form.html', {'form': form})
        # except Exception as e:
        #     return render(request, {"error_message": "unexpected error occured"}, 'error.html')

    def post(self, request):
        # try:
        form = ScoresForm(request.POST, request.FILES)
        if form.is_valid():
            # import pdb;pdb.set_trace()
            form.save()
            return redirect('scores_list')
        return render(request, 'scores_form.html', {'form': form})
        # except ValidationError as e: 
        #     return render(request, 'error.html', {"error_message": "Validation error occurred"})
        # except Exception as e:
        #     return render(request, {"error_message": "unexpected error occured"}, 'error.html')
    
class ScoresAddView(View):
    def get(self, request):
        try:
            form = ScoresAddForm()
            return render(request, 'scores_form.html', {'form': form})
        except Scores.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')

    def post(self, request):
        try:
            form = ScoresAddForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('scores_list')
            return render(request, 'scores_form.html', {'form': form})
        except ValidationError as e:
            return render(request, 'error.html', {"error_message": "Validation error occurred"})
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')

class ScoresUpdateView(View):
    def get(self, request, id):
        try:
            score = Scores.objects.get(id=id)
            form = ScoresUpdateForm(instance=score)
            return render(request, 'scores_form.html', {'form': form})
        except Scores.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')

    def post(self, request, id):
        try:
            score = Scores.objects.get(id=id)
            form = ScoresUpdateForm(request.POST, instance=score)
            if form.is_valid():
                form.save()
                return redirect('scores_list')
            return render(request, 'scores_form.html', {'form': form})
        except Scores.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')

class ScoresDeleteView(View):
    def get(self, request, id):
        try:
            score = Scores.objects.get(id=id)
            return render(request, 'scores_confirm_delete.html', {'score': score})
        except Scores.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')

    def post(self, request, id):
        try:
            score = Scores.objects.get(id=id)
            score.delete()
            return redirect('scores_list')
        except Scores.DoesNotExist:
            return render(request, {"error_message": "error retriving teacher data"}, 'error.html')
        except Exception as e:
            return render(request, {"error_message": "unexpected error occured"}, 'error.html')

class ScoreFileView(View):
    def get(self, request, pk):
        # Correctly fetch the score object
        score = get_object_or_404(Scores, pk=pk)

        # Ensure file exists
        if not score.file_upload:
            return HttpResponse("No file found for this assignment.", content_type="text/plain")

        # Return file response for download or viewing in browser
        try:
            file_path = score.file_upload.path
            return FileResponse(open(file_path, 'rb'), as_attachment=False)  # Use True for download
        except FileNotFoundError:
            raise Http404("File not found.")
        except Exception as e:
            return HttpResponse(f"Error opening file: {str(e)}", content_type="text/plain")