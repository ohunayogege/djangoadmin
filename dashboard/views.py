from django.shortcuts import render, get_object_or_404, redirect
from .models import User, LoginCount
import datetime
from django.utils import timezone
from datetime import timedelta
from django.contrib import auth
from djangoadmin import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import auth
from django.http import HttpResponse
from django.template.loader import render_to_string
from .forms import EmailForm, EmailUserForm



def index(request):
	if request.user.is_authenticated:
		return redirect('home')
	return render(request, 'index.html')

@login_required
def home(request):
	user = request.user
	logins = LoginCount.objects.all().filter(log_user=request.user)
	user_count = User.objects.all().count()
	nuser_count = User.objects.all().exclude(is_staff=True).count()
	staff_count = User.objects.filter(is_superuser=True, is_staff=True).count()
	return render(request, 'home.html', {'user_count': user_count, 'staff_count': staff_count, 'nuser_count': nuser_count, 'logins':logins})

@login_required
def reg_user_last_24(request):
	form = EmailUserForm()
	success = ''
	error = ''
	message = ''
	if request.method == 'POST':
		form = EmailUserForm(request.POST)
		if form.is_valid():
		    subject = form.cleaned_data['subject']
		    content = form.cleaned_data['content']
		    email = form.cleaned_data['email']
		    sent = send_mail(subject, content, settings.EMAIL_HOST_USER, [email], fail_silently=True)
		    if sent:
		    	success = "Message Sent Successfully."
		    else:
		    	print("Hey:::::::::::::::::::   Hmmmmmmmmmmmmmmmmm")
		    	error = "Message Not Sent. Please Try Again Later!!"
		else:
			message = "Please Check if all fields are filled correctly."
	return render(request, 'reg_user_last_24.html', {'error': error, 'success': success, 'message': message, 'message': message, 'form':form})

@login_required
def reg_user_last_week(request):
	form = EmailUserForm()
	success = ''
	error = ''
	message = ''
	if request.method == 'POST':
		form = EmailUserForm(request.POST)
		if form.is_valid():
		    subject = form.cleaned_data['subject']
		    content = form.cleaned_data['content']
		    email = form.cleaned_data['email']
		    sent = send_mail(subject, content, settings.EMAIL_HOST_USER, email, fail_silently=True)
		    if sent:
		    	success = "Message Sent Successfully."
		    else:
		    	print("Hey:::::::::::::::::::   Hmmmmmmmmmmmmmmmmm")
		    	error = "Message Not Sent. Please Try Again Later!!"
		else:
			message = "Please Check if all fields are filled correctly."
	return render(request, 'reg_user_last_week.html', {'error': error, 'success': success, 'message': message, 'message': message, 'form':form})

@login_required
def reg_user_last_month(request):
	form = EmailUserForm()
	success = ''
	error = ''
	message = ''
	if request.method == 'POST':
		form = EmailUserForm(request.POST)
		if form.is_valid():
		    subject = form.cleaned_data['subject']
		    content = form.cleaned_data['content']
		    email = form.cleaned_data['email']
		    sent = send_mail(subject, content, settings.EMAIL_HOST_USER, email, fail_silently=True)
		    if sent:
		    	success = "Message Sent Successfully."
		    else:
		    	print("Hey:::::::::::::::::::   Hmmmmmmmmmmmmmmmmm")
		    	error = "Message Not Sent. Please Try Again Later!!"
		else:
			message = "Please Check if all fields are filled correctly."
	return render(request, 'reg_user_last_month.html', {'error': error, 'success': success, 'message': message, 'message': message, 'form':form})

@login_required
def deactivate(request):
	return render(request, 'deactivate_user.html')

@login_required
def deactivate_user(request, username):
	user = get_object_or_404(User, username=username)
	# user = User.objects.get(username = request.user.profile.user_id)
	try:
		user.is_active = False
		user.save()
	except:
		# messages.error(request,'Please try again.')
		return redirect('deactivate')

	# messages.success(request, 'User successfully deactivated.')
	return render(request, 'deactivate_user.html')

@login_required
def activate_user(request, username):
	user = get_object_or_404(User, username=username)
	# user = User.objects.get(username = request.user.profile.user_id)
	try:
		user.is_active = True
		user.save()
	except:
		# messages.error(request,'Please try again.')
		return redirect('deactivate')

	# messages.success(request, 'User successfully deactivated.')
	return render(request, 'deactivate_user.html')

@login_required
def admins(request):
	form = EmailUserForm()
	success = ''
	error = ''
	message = ''
	if request.method == 'POST':
		form = EmailUserForm(request.POST)
		if form.is_valid():
		    subject = form.cleaned_data['subject']
		    content = form.cleaned_data['content']
		    email = form.cleaned_data['email']
		    sent = send_mail(subject, content, settings.EMAIL_HOST_USER, [email], fail_silently=True)
		    if sent:
		    	success = "Message Sent Successfully."
		    else:
		    	print("Hey:::::::::::::::::::   Hmmmmmmmmmmmmmmmmm")
		    	error = "Message Not Sent. Please Try Again Later!!"
		else:
			message = "Please Check if all fields are filled correctly."
	return render(request, 'admins.html', {'error': error, 'success': success, 'message': message, 'message': message, 'form':form})

@login_required
def users(request):
	form = EmailUserForm()
	success = ''
	error = ''
	message = ''
	if request.method == 'POST':
		form = EmailUserForm(request.POST)
		if form.is_valid():
		    subject = form.cleaned_data['subject']
		    content = form.cleaned_data['content']
		    email = form.cleaned_data['email']
		    sent = send_mail(subject, content, settings.EMAIL_HOST_USER, [email], fail_silently=True)
		    if sent:
		    	success = "Message Sent Successfully."
		    else:
		    	print("Hey:::::::::::::::::::   Hmmmmmmmmmmmmmmmmm")
		    	error = "Message Not Sent. Please Try Again Later!!"
		else:
			message = "Please Check if all fields are filled correctly."
	return render(request, 'users.html', {'error': error, 'success': success, 'message': message, 'message': message, 'form':form})

@login_required
def staffs(request):
	form = EmailUserForm()
	success = ''
	error = ''
	message = ''
	if request.method == 'POST':
		form = EmailUserForm(request.POST)
		if form.is_valid():
		    subject = form.cleaned_data['subject']
		    content = form.cleaned_data['content']
		    email = form.cleaned_data['email']
		    sent = send_mail(subject, content, settings.EMAIL_HOST_USER, [email], fail_silently=True)
		    if sent:
		    	success = "Message Sent Successfully."
		    else:
		    	print("Hey:::::::::::::::::::   Hmmmmmmmmmmmmmmmmm")
		    	error = "Message Not Sent. Please Try Again Later!!"
		else:
			message = "Please Check if all fields are filled correctly."
	return render(request, 'staffs.html', {'error': error, 'success': success, 'message': message, 'message': message, 'form':form})

@login_required
def profile(request, username):
	user = get_object_or_404(User, username=username)
	user = request.user
	logins = LoginCount.objects.all().filter(log_user=request.user)
	# print("User Joined on::::", user.joined_date)
	return render(request,'profile.html',{'user':user, 'logins':logins})

def login(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
	    message = ''
	    if request.method == 'POST':
	        email = request.POST.get('email')
	        password = request.POST.get('password')
	        user = auth.authenticate(email=email, password=password)

	        if user is not None:
	            # correct username and password login the user
	            auth.login(request, user)
	            get_user = User.objects.get(id=user.id)
	            get_log_count = get_user.logins
	            new_log_count = get_log_count + 1
	            User.objects.filter(id=user.id).update(logins=new_log_count)
	            user_ip = request.META.get("REMOTE_ADDR")
	            user_browser = request.META.get("HTTP_USER_AGENT")
	            LoginCount.objects.create(log_user=user, browser=user_browser, ip_address=user_ip)
	            return redirect('home')
	        else:
	            message = 'Incorrect Email/Password'

	return render(request, 'login.html', {'message': message})


@login_required
def sendmail(request):
	form = EmailForm()
	success = ''
	error = ''
	message = ''
	if request.method == 'POST':
		form = EmailForm(request.POST)
		if form.is_valid():
		    subject = form.cleaned_data['subject']
		    content = form.cleaned_data['content']
		    users = User.objects.all().exclude(is_superuser=True, is_staff=True)
		    to = []
		    for user in users:
		    	to.append(user.email)
		    # send_mail(subject, message, sender, recipients)
		    sent = send_mail(subject, content, settings.EMAIL_HOST_USER, to, fail_silently=True)
		    if sent:
		    	print("Hey:::::::::::::::::::   Hmmmmmmmmmmmmmmmmm")
		    	success = "Message Sent Successfully."
		    else:
		    	error = "Message Not Sent. Please Try Again Later or Check your mail settings in settings.py"
		else:
			message = "Please Check if all fields are filled correctly."
	return render(request, 'send_mail.html', {'error': error, 'success': success, 'message': message, 'message': message, 'form':form})

# @login_required
# def singlemail(request):
# 	return render(request, 'send_mail.html')
