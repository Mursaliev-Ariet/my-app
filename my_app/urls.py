from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('students/', views.student_list, name='students_list'),
    path('teachers/', views.teacher_list, name='teachers_list'),
    path('groups/', views.group_list, name='groups_list'),
    path('subjects/', views.subject_list, name='subjects_list'),
    path('homeworks/', views.homework_list, name='homeworks_list'),
    path('clients/', views.client_list, name='clients_list'),
]