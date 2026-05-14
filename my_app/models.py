from django.db import models

class Student(models.Model):
    last_name = models.CharField(max_length=100, verbose_name="имя")
    first_name = models.CharField(max_length=100, verbose_name="фамилия")
    age = models.IntegerField(verbose_name="возраст")

    def __str__(self):
        return self.last_name
    class Meta:
        verbose_name = "студент"
        verbose_name_plural = "студент"

class Teacher(models.Model):
    username = models.CharField(max_length=100, verbose_name="имя")
    password = models.CharField(max_length=100, verbose_name="пароль")
    money = models.IntegerField(verbose_name="заработок")
    age = models.IntegerField(verbose_name="возраст")

    def __str__(self):
        return self.username
    class Meta:
        verbose_name = "учитель"
        verbose_name_plural = "учитель"

class Group(models.Model):
    username = models.CharField(max_length=100, verbose_name="имя")
    password = models.CharField(max_length=100, verbose_name="пароль")

    def __str__(self):
        return self.username
    class Meta:
        verbose_name = "группа"
        verbose_name_plural = "группа"

class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name="предмет")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "предмет"
        verbose_name_plural = "предмет"


class Homework(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа")
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, verbose_name="Учитель")
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание задания")
    deadline = models.DateTimeField(verbose_name="Срок сдачи")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "домашнее задание"
        verbose_name_plural = "домашнее задание"