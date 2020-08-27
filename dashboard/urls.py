from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from django.conf import settings
from . import views


urlpatterns = [
	# url(r'^login/$', django.contrib.auth.views.LoginView),
 #    url(r'^logout/$', django.contrib.auth.views.LogoutView),
 	url( r'^login.html$', views.login, name="login"),
	url(r'^admin.html$', views.home, name='home'),
	url(r'^index.html$', views.index, name='index'),
	url(r'^$', views.index, name='index'),
	url(r'^reg_user_last_24.html$', views.reg_user_last_24, name='reg_user_last_24'),
	url(r'^reg_user_last_week.html$', views.reg_user_last_week, name='reg_user_last_week'),
	url(r'^reg_user_last_month.html$', views.reg_user_last_month, name='reg_user_last_month'),
	url(r'^users/admins.html$', views.admins, name='admins'),
	url(r'^users/staffs.html$', views.staffs, name='staffs'),
	url(r'^users.html$', views.users, name='users'),
	url(r'^profile/(?P<username>\w+).html$', views.profile, name='profile'),
	url(r'^deactivate_user/(?P<username>\w+).html$', views.deactivate_user, name='deactivate_user'),
	url(r'^activate_user/(?P<username>\w+).html$', views.activate_user, name='activate_user'),
	url(r'^deactivate_user.html$', views.deactivate, name='deactivate'),
	url(r'^send_mail.html$', views.sendmail, name='send_mail'),

	####
	# re_path(r'^register/$', register_view, name='signup'),
 #    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
 #            activate, name='users_activate'),
 #    re_path('login/', auth_views.LoginView, {
 #        'template_name': "users/registration/login.html"},
 #        name='login'),
    re_path(r'^logout.html$', auth_views.LogoutView.as_view(),
        {'next_page': settings.LOGIN_REDIRECT_URL}, name='logout'),

 #    re_path(r'^password_reset/$', auth_views.PasswordResetView,
 #        {'template_name': "users/registration/password_reset_form.html"},
 #        name='password_reset'),
 #    re_path(r'^password_reset/done/$', auth_views.PasswordResetDoneView,
 #        {'template_name': "users/registration/password_reset_done.html"},
 #        name='password_reset_done'),
 #    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
 #        auth_views.PasswordResetConfirmView,
 #        {'template_name': "users/registration/password_reset_confirm.html"},
 #        name='password_reset_confirm'),
 #    re_path(r'^reset/done/$', auth_views.PasswordResetCompleteView,
 #        {'template_name': "users/registration/password_reset_complete.html"},
 #        name='password_reset_complete'),
]
