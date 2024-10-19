from django import forms
from .models import UserProfile

class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'dob', 'gender', 'address', 'city_id', 'email', 'start_date', 'job_title', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
