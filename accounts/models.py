from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=200)


'''class CompanyAccount(models.Model):
    company_name = models.CharField(max_length=300)
    recruiter_name = models.CharField(max_length=200)
    email = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Training(models.Model):
    title = models.CharField(max_length=1000)
    company = models.ForeignKey(CompanyAccount, on_delete=models.CASCADE)
    time_period = models.IntegerField


YEAR_CHOICES = (
    2016,
    2017,
    2018,
    2019,
)
    batch = models.CharField(max_length=4, choices=YEAR_CHOICES, default='2017')




class Student(models.Model):
    # Convert most fields to DROPDOWN

    # personal details
    name = models.CharField(max_length=300)

    # Contact details
    mob_no = models.IntegerField()
    email = models.CharField(max_length=300)

    # Academic details
    uni_roll = models.IntegerField()
    department = models.CharField(max_length=300)
    course = models.CharField(max_length=300)
    batch = models.IntegerField()
    backlogs = models.IntegerField()
    resume = models.FileField()

    def year(self):
        now = datetime.datetime.now()
        return now.year-self.batch
'''
