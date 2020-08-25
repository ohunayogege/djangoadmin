from django.shortcuts import render, get_object_or_404
from .models import User
import datetime
from django.utils import timezone
from datetime import timedelta
from django.contrib import auth
# from .forms import (DeactivateProfileForm, ProfileForm)
from django.contrib.auth.decorators import login_required
from django.contrib import auth


@login_required
def home(request):
	return render(request, 'home.html')

@login_required
def reg_user_last_24(request):
	return render(request, 'reg_user_last_24.html')

@login_required
def reg_user_last_week(request):
	return render(request, 'reg_user_last_week.html')

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
def reg_user_last_month(request):
	return render(request, 'reg_user_last_month.html')

@login_required
def admins(request):
	return render(request, 'admins.html')

@login_required
def users(request):
	return render(request, 'users.html')

@login_required
def staffs(request):
	return render(request, 'staffs.html')

@login_required
def profile(request, username):
	user = get_object_or_404(User, username=username)
	# print("User Joined on::::", user.joined_date)
	return render(request,'profile.html',{'user':user})

def login(request):
    if request.user.is_authenticated():
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

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
            messages.error(request, 'Error wrong username/password')

    return render(request, 'blog/login.html')

def logout(request):
    auth.logout(request)
    return render(request,'index.html')
