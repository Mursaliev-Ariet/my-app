from django.shortcuts import render
from .models import *
from django.db.models import Q

def student_list(request):
    students_list = Student.objects.all()
    return render(request, 'students/list.html', {'students_list': students_list})


def teacher_list(request):
    teachers_list = Teacher.objects.all()
    return render(request, 'teachers/list.html', {'teachers_list': teachers_list})


def group_list(request):
    groups_list = Group.objects.all()
    return render(request, 'groups/list.html', {'groups_list': groups_list})


def subject_list(request):
    subjects_list = Subject.objects.all()
    return render(request, 'subjects/list.html', {'subjects_list': subjects_list})

def homework_list(request):
    homeworks_list = Homework.objects.all()
    return render(request, 'homeworks/list.html', {'homeworks_list': homeworks_list})

def client_list(request):
    search = request.GET.get('search')

    if search:
        clients_list = Client.objects.filter(
            Q(name__icontains=search) |
            Q(surname__icontains=search) |
            Q(number__icontains=search)
        )
    else:
        clients_list = Client.objects.all()

    return render(request, 'Clients/list.html', {
        'clients_list': clients_list
    })