from django.urls import path

from . import views

urlpatterns = [
    path("teacher_signup/", views.teacherSignUp.as_view(), name="teacher_signup"),
    path("student_signup/", views.studentSignUp.as_view(), name="student_signup"),
    path("student_list/", views.student_list.as_view(), name="student_list"),
    path("student_detail/", views.studentDetail.as_view(), name="student_detail"),
]