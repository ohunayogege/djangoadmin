from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, MailSent, LoginCount


admin.site.site_header = 'Django Dashboard'
# Register your models here.
admin.site.register(MailSent)
admin.site.register(User)
admin.site.register(LoginCount)
admin.site.unregister(Group)
