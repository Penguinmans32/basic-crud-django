from django.shortcuts import render, redirect


from .models import EmployementTerms
from .forms import EmploymentTermsForm

# Create your views here.

def term_list(request):
    terms = EmployementTerms.objects.all()
    return render(request, 'terms_list.html', {'terms': terms})

def terms_create(request):
    if request.method == 'POST':
        form = EmploymentTermsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('terms_list')
    else:
        form = EmploymentTermsForm()
    return render(request, 'terms.create.html', {'form': form})

def terms_update(request, pk):
    term = EmployementTerms.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmploymentTermsForm(request.POST, instance=term)
        if form.is_valid():
            form.save()
            return redirect('terms_list')
    else:
        form = EmploymentTermsForm(instance=term)
    return render(request, 'terms_form.html', {'form': form})

def terms_delete(request, pk):
    term = EmployementTerms.objects.get(pk=pk)
    if request.method == 'POST':
        term.delete()
        return redirect('terms_list')
    return render(request, 'terms_confirm_delete.html', {'term': term})
