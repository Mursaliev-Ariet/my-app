from django.db import models

class Student(models.Model):
    last_name = models.CharField(max_length=100, verbose_name="имя")
    first_name = models.CharField(max_length=100, verbose_name="пароль")
    age = models.CharField(max_length=100, verbose_name="возраст")


class Teacher(models.Model):
    username = models.CharField(max_length=100, verbose_name="имя")
    password = models.CharField(max_length=100, verbose_name="пароль")
    money = models.CharField(max_length=100, verbose_name="заработок")
    age = models.CharField(max_length=100, verbose_name="возраст")


from django.db import models
class Group(models.Model):
    username = models.CharField(max_length=100, verbose_name="имя")
    password = models.CharField(max_length=100, verbose_name="пароль")


from django.db import models
class Director(models.Model):
    username = models.CharField(max_length=100, verbose_name="имя")
    password = models.CharField(max_length=100, verbose_name="пароль")


from django.db import models
class School(models.Model):
    username = models.CharField(max_length=100, verbose_name="имя")
    password = models.CharField(max_length=100, verbose_name="пароль")
def __str__(self):
    return self.username
class Meta:
    db_table = 'Student'