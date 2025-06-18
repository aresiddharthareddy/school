from django.urls import path
from .views import (
    TeacherListView, TeacherCreateView, TeacherUpdateView, TeacherDeleteView,
    StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView, AssignmentListView, AssignmentCreateView, AssignmentUpdateView, AssignmentDeleteView, AssignmentSubmitView,AssignmentFileView, ScoreFileView,
    ScoresListView, ScoresCreateView, ScoresUpdateView, ScoresDeleteView, login_user, logout_user, admin_dashboard,  logout_teacher, logout_student, StudentSubjectView, ScoresAddView, Admin_dashboardView
)

urlpatterns = [
    #login URLs
    path("", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("admin_dashboard/", admin_dashboard, name="admin_dashboard"),
    path("logout/teacher/", logout_teacher, name="logout_teacher"),
    path("logout/student/", logout_student, name="logout_student"),


    # Teacher URLs
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teachers/add/', TeacherCreateView.as_view(), name='teacher_create'),
    path('teachers/edit/<int:id>/', TeacherUpdateView.as_view(), name='teacher_update'),
    path('teachers/delete/<int:id>/', TeacherDeleteView.as_view(), name='teacher_delete'),


    # Student URLs
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/add/', StudentCreateView.as_view(), name='student_add'),
    path('students/edit/<int:id>/', StudentUpdateView.as_view(), name='student_update'),
    path('students/sub/<int:id>/', StudentSubjectView.as_view(), name='student_sub'),
    path('students/delete/<int:id>/', StudentDeleteView.as_view(), name='student_delete'),

     # Assignments URLs
    path('assignments/', AssignmentListView.as_view(), name='assignment_list'),
    path('assignments/add/', AssignmentCreateView.as_view(), name='assignment_add'),
    path('assignments/edit/<int:id>/', AssignmentUpdateView.as_view(), name='assignment_edit'),
    path('assignments/delete/<int:id>/', AssignmentDeleteView.as_view(), name='assignment_delete'),
    path('assignments/submit/<int:id>/', AssignmentSubmitView.as_view(), name='assignment_submit'),
    path('assignment-file/<int:pk>/', AssignmentFileView.as_view(), name='assignment_file'),

    

    path('scores/', ScoresListView.as_view(), name='scores_list'),
    path('scores/add/', ScoresCreateView.as_view(), name='scores_add'),
    path('scoresadd/add', ScoresAddView.as_view(), name= 'scoresadd_add'),
    path('scores/update/<int:id>', ScoresUpdateView.as_view(), name='scores_update'),
    path('score-file/<int:pk>/', ScoreFileView.as_view(), name='score_file'),
    

]