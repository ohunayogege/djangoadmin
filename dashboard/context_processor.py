from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
from datetime import timedelta


def users(request):
    users = User.objects.all().exclude(is_staff=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(users, 5)

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return {
        'users': users,
    }

def admins(request):
    admins = User.objects.all().filter(is_superuser=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(admins, 5)

    try:
        admins = paginator.page(page)
    except PageNotAnInteger:
        admins = paginator.page(1)
    except EmptyPage:
        admins = paginator.page(paginator.num_pages)

    return {
        'admins': admins,
    }

def staffs(request):
    staffs = User.objects.all().filter(is_staff=True).exclude(is_superuser=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(staffs, 5)

    try:
        staffs = paginator.page(page)
    except PageNotAnInteger:
        staffs = paginator.page(1)
    except EmptyPage:
        staffs = paginator.page(paginator.num_pages)

    return {
        'staffs': staffs,
    }

def reg_user_last_24(request):
	# date = User.objects.all()
	# print(user)
	current_date = datetime.date.today()
	tdate = current_date
	yesterday = tdate - datetime.timedelta(hours=24)
	# yesterday = current_week + datetime.timedelta(1)
	# yesterday = today

	reg_user_last_24 = User.objects.all().exclude(joined_date__lt=yesterday).filter(joined_date__gte=yesterday)
	page = request.GET.get('page', 1)
	paginator = Paginator(reg_user_last_24, 5)

	try:
		reg_user_last_24 = paginator.page(page)
	except PageNotAnInteger:
		reg_user_last_24 = paginator.page(1)
	except EmptyPage:
		reg_user_last_24 = paginator.page(paginator.num_pages)

	return {
		'reg_user_last_24': reg_user_last_24,
	}

def reg_user_last_week(request):
	# date = User.objects.all()
	# print(user)
	current_date = datetime.date.today()
	tdate = current_date
	# current_week = tdate - datetime.timedelta(tdate.weekday())
	last_week = tdate - datetime.timedelta(weeks=1)

	reg_user_lastweek = User.objects.all().exclude(joined_date__lt=last_week).filter(joined_date__gte=last_week)
	page = request.GET.get('page', 1)
	paginator = Paginator(reg_user_lastweek, 5)

	try:
		reg_user_lastweek = paginator.page(page)
	except PageNotAnInteger:
		reg_user_lastweek = paginator.page(1)
	except EmptyPage:
		reg_user_lastweek = paginator.page(paginator.num_pages)

	return {
		'reg_user_lastweek': reg_user_lastweek,
	}

def reg_user_last_month(request):
	# date = User.objects.all()
	# print(user)
	current_date = datetime.date.today()
	tdate = current_date
	# current_month = tdate - datetime.timedelta(tdate.weekday())
	last_month = tdate - datetime.timedelta(weeks=4)
	print("Hey::::  ", last_month)

	reg_user_lastmonth = User.objects.all().exclude(joined_date__lt=last_month).filter(joined_date__gte=last_month)
	page = request.GET.get('page', 1)
	paginator = Paginator(reg_user_lastmonth, 5)

	try:
		reg_user_lastmonth = paginator.page(page)
	except PageNotAnInteger:
		reg_user_lastmonth = paginator.page(1)
	except EmptyPage:
		reg_user_lastmonth = paginator.page(paginator.num_pages)

	return {
		'reg_user_lastmonth': reg_user_lastmonth,
	}

def all_users(request):
    all_users = User.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(all_users, 5)

    try:
        all_users = paginator.page(page)
    except PageNotAnInteger:
        all_users = paginator.page(1)
    except EmptyPage:
        all_users = paginator.page(paginator.num_pages)

    return {
        'all_users': all_users,
    }

# def logins(request):
# 	if request.user.is_authenticated:
# 		user = request.user
# 		logins = LoginCount.objects.all().filter(log_user=request.user)
# 		page = request.GET.get('page', 1)
# 		paginator = Paginator(logins, 5)

# 		try:
# 		    logins = paginator.page(page)
# 		except PageNotAnInteger:
# 		    logins = paginator.page(1)
# 		except EmptyPage:
# 		    logins = paginator.page(paginator.num_pages)

# 		return {
# 		    'logins': logins,
# 		}
