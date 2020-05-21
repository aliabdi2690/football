from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from .forms import SignUpForm, LoginForm
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .tokens import acc_active_token
from django.core.mail import EmailMessage
from .models import MyUsermodel
from django.contrib.auth import login, authenticate
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = "activate your fotball account"
            message = render_to_string('acc_active_mail.html', {
                'user':user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':acc_active_token.make_token(user)
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return render(request, 'home.html', {'message':"check your email"})
        else:
            return render(request,'signup.html' ,{'message':"check your inputs", 'form':form})
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form':form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = MyUsermodel.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError,):
        user = None
    if user is not None and acc_active_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request,user)
        return redirect('/')
    else:
        return render(request, 'signup.html', {'message':"invalid link"})

def logein(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                    login(request, user)
                    return redirect('/')
            else:
                return render(request, 'logein.html', {'form':form, 'message':"email is wrong"})
        else:
            return render(request, 'logein.html', {'form':form, 'message':"invalid inputs"})
    else:
        form = LoginForm()
        return render(request, 'logein.html', {'form':form})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')