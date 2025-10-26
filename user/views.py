from django.shortcuts import render, redirect
from django.views.generic import View
from .models import CustomUser
from django.contrib.auth import login, authenticate

class StepOneRegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'user/register-step-one.html')

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        if CustomUser.objects.filter(email=email).exists():
            return render(request, 'user/register-step-one.html', {'error': 'Email already exists.'})

        request.session['registration_email'] = email
        request.session['valid_step_one'] = True
        return redirect('user:register-step-two')

class StepTwoRegisterView(View):
    def get(self, request, *args, **kwargs):
        if not request.session.get('valid_step_one'):
            return redirect('user:register-step-one')
        return render(request, 'user/register-step-two.html')

    def post(self, request, *args, **kwargs):
        if not request.session.get('valid_step_one'):
            return redirect('user:register-step-one')

        username = request.POST.get('username')
        if CustomUser.objects.filter(username=username).exists():
            return render(request, 'user/register-step-two.html', {'error': 'Username already exists.'})

        request.session['registration_username'] = username
        request.session['valid_step_two'] = True
        return redirect('user:register-step-three')
    
class StepThreeRegisterView(View):
    def get(self, request, *args, **kwargs):
        if not request.session.get('valid_step_two'):
            return redirect('user:register-step-two')
        return render(request, 'user/register-step-three.html')

    def post(self, request, *args, **kwargs):
        if not request.session.get('valid_step_two'):
            return redirect('user:register-step-two')

        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            return render(request, 'user/register-step-three.html', {'error': 'Passwords do not match.'})

        email = request.session.get('registration_email')
        username = request.session.get('registration_username')

        if CustomUser.objects.filter(email=email).exists() or CustomUser.objects.filter(username=username).exists():
            request.session.flush()
            return redirect('user:register-step-one')

        user = CustomUser.objects.create_user(username=username, email=email, password=password)

        for key in ['registration_email', 'registration_username', 'valid_step_one', 'valid_step_two']:
            if key in request.session:
                del request.session[key]

        return render(request, 'user/registration_complete.html')
        

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'user/login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog:home')
        else:
            return render(request, 'user/login.html', {'error': 'Invalid username or password.'})