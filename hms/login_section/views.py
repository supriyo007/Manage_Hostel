from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from login_section.forms import SignUpForm

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()
            # user.student.dob=form.cleaned_data.get('dob')
            user.save()
            username=form.cleaned_data.get('usernmae')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form=SignUpForm()
    return render(request, 'signup.html', {'form':form})



