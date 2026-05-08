from django.db import models

class Student(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    age = models.EmailField(max_length=100)


from django.db import models

class Teacher(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    money = models.CharField(max_length=100)
    age = models.EmailField(max_length=100)
    def __str__(self):
        return self.username


    class Meta:
        db_table = 'Student'
