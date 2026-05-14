from django.shortcuts import render
from my_app.models import Student, Teacher, Group, Subject, Homework


def home(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    groups = Group.objects.all()
    subjects = Subject.objects.all()
    homeworks = Homework.objects.all()

    context = {
        'students': students,
        'teachers': teachers,
        'groups': groups,
        'subjects': subjects,
        'homeworks': homeworks,
    }

    return render(request, 'home.html', context)
