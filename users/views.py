from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from .forms import SignUpForm
from django.contrib.auth import authenticate, login

# Sign Up View
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = UserProfile.objects.filter(email=email, password=password).first()
        if user:
            # Log in user
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

# Home (Dashboard) View
def home_view(request):
    users = UserProfile.objects.all()
    return render(request, 'home.html', {'users': users})

# Update User View
def update_user(request, user_id):
    user = get_object_or_404(UserProfile, pk=user_id)
    if request.method == 'POST':
        form = SignUpForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm(instance=user)
    return render(request, 'update.html', {'form': form})

# Delete User View
def delete_user(request, user_id):
    user = get_object_or_404(UserProfile, pk=user_id)
    user.delete()
    return redirect('home')

@staff_member_required
def admin_view(request):
    users = UserProfile.objects.all()
    return render(request, 'admin.html', {'users': users})