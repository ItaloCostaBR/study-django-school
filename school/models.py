from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    date_of_birth = models.DateField()

    def __str__(self):
        return f'{self.cpf} - {self.name}'

class Course(models.Model):
    LEVELS = (
        ('B', 'Basic'),
        ('I', 'Intermediary'),
        ('A', 'Advanced'),
    )
    id = models.AutoField(primary_key=True)
    cod_course = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    level = models.CharField(max_length=1, choices=LEVELS, blank=False, null=False, default='B')

    def __str__(self):
        return f'{self.description} - {self.cod_course}'

class Registration(models.Model):
    PERIOD = (
        ('M', 'Morning'),
        ('E', 'Evening'),
        ('N', 'Nocturnal'),
    )
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    period = models.CharField(max_length=1, choices=PERIOD, blank=False, null=False, default='M')

    def __str__(self):
        return f'{self.student.name} - {self.course.cod_course} - {self.period}'
