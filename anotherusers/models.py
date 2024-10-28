from django.db import models

# Create your models here.

class EmployementTerms(models.Model):
    employee_id = models.IntegerField()
    agreed_salary = models.FloatField()
    salary_start_date = models.DateField()
    salary_end_date = models.DateField()

    def __str__(self):
        return f"{self.employee_id}:{ self.agreed_salary}"
