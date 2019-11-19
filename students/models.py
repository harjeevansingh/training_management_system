from django.db import models
from django.contrib.auth.models import User



'''class Student(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name'''


class Training(models.Model):
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=300)
    company_name = models.CharField(max_length=300)
    place = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.company_name


class Project(models.Model):
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # training_id = models.ForeignKey(Training, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=300)
    description = models.CharField(max_length=2000)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.project_name

    def summary(self):
        return self.description[:100]


class WorkUpdates(models.Model):
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    training_id = models.ForeignKey(Training, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    date = models.DateField()

    def title(self):
        return self.description[0:75]

    def __str__(self):
        return self.name


