# forms.py
from django import forms
from .models import EmployementTerms

class EmploymentTermsForm(forms.ModelForm):
    class Meta:
        model = EmployementTerms
        fields = ['employee_id', 'agreed_salary', 'salary_start_date', 'salary_end_date']
        widgets = {
            'salary_start_date': forms.DateInput(attrs={'type': 'date'}),
            'salary_end_date': forms.DateInput(attrs={'type': 'date'}),
        }
