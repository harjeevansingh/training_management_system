from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Training(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    role_tech = models.CharField(max_length=300)
    company_name = models.CharField(max_length=300)
    place = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.company_name


class Project(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    training_id = models.ForeignKey(Training, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=300)
    description = models.CharField(max_length=2000)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.project_name

