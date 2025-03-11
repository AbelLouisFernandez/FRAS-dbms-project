from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser,Booking
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from  .forms import SignUpForm,BookingForm
from django.db.models import Q
import random
from django_ratelimit.decorators import ratelimit
from django.contrib.auth.views import PasswordResetView
#from verify_email.email_handler import *
import verify_email
from django.core.mail import send_mail
from verify_email.email_handler import ActivationMailManager


def home(request):
  context = {}
  return render(request,'base/home.html',context)
def profile(request):
    user=request.user
    context={'user':user}
    return render(request,'base/profile.html',context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            enteredemail=form.cleaned_data['email']
            users = CustomUser.objects.filter(email=enteredemail).first()

            if users:
                messages.error(request, 'This email has already been registered to a user')
            else:
                if form.cleaned_data['avatar']:
                    pass
                else:
                    form.cleaned_data['avatar']='avatar.png'
                    mail_manager = ActivationMailManager()
                    inactive_user = mail_manager.send_verification_link(form=form)
                    return render(request,'base/verificationemailsent.html')
    else:
        form = SignUpForm()

    return render(request, 'base/signup.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import CustomUser

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # ✅ Correct usage of authenticate()
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password is incorrect')

    context = {'page': page}
    return render(request, 'base/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')

def handler500(exception):
    response = render(exception,template_name='base/404.html')
    response.status_code = 500
    return response
def handler400(request, exception):
    response = render(request,template_name='base/404.html')
    response.status_code = 400
    return response
def handler404(request, exception):
    response = render(request,template_name='base/404.html')
    response.status_code = 400
    return response
class CustomPasswordResetView(PasswordResetView):
    template_name='base/registration/password_reset.html'
    email_template_name = 'base/registration/password_reset_email.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data['email']
        self.extra_context = {'email': email}
        return response

@ratelimit(key='ip', rate='2/h', method='POST')  # if users are behind a shared IP (such as in some corporate or public networks)
def custom_password_reset_view(request, *args, **kwargs):
    return CustomPasswordResetView.as_view()(request, *args, **kwargs)


@login_required
def book_ambulance(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()

            # Send Email to Coordinator
            coordinator_email = "abellouisfernandez@gmail.com"
            subject = "🚑 New Ambulance Booking Request"
            message = f"""
            A new ambulance booking has been made by {request.user.username}.
            Location: https://www.google.com/maps?q={booking.latitude},{booking.longitude}
            """
            send_mail(subject, message, "your_email@example.com", [coordinator_email])

            return redirect("success_page")  # Redirect to a success page
    else:
        form = BookingForm()

    return render(request, "base/book_ambulance.html", {"form": form})

def success_page(request):
    return render(request, "base/success.html")


