from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


class UserManager(BaseUserManager):
    def create_user(
            self, username, email, first_name, last_name, password=None,
            commit=True):
        """
        Creates and saves a User with the given email, first name, last name
        and password.
        """
        if not username:
            raise ValueError(_('Users must have username'))
        if not email:
            raise ValueError(_('Users must have an email address'))
        if not first_name:
            raise ValueError(_('Users must have a first name'))
        if not last_name:
            raise ValueError(_('Users must have a last name'))

        user = self.model(
        	username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        if commit:
            user.save(using=self._db)
        return user

    def create_superuser(self, username, email, first_name, last_name, password):
        """
        Creates and saves a superuser with the given email, first name,
        last name and password.
        """
        user = self.create_user(
            username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            commit=False,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_('email address'), max_length=255, unique=True
    )
    username = models.CharField(_('Username'), max_length=100, default='', unique=True)
    # password field supplied by AbstractBaseUser
    # last_login field supplied by AbstractBaseUser
    first_name = models.CharField(_('first name'), max_length=30, blank=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False)
    gender = models.CharField(_('gender'), choices=GENDER, max_length=10, blank=False, default='')
    photo = models.ImageField(verbose_name=_('profile photo'), upload_to='users', default='', blank=True)
    mobile = models.CharField(verbose_name=_('Mobile Number'), max_length=21, unique=True, default='')
    # Locations
    state = models.CharField(verbose_name=_('current state'), max_length=30, blank=True, default='')
    lga = models.CharField(verbose_name=_('Local Government Area'), max_length=50, blank=True, default='')
    city = models.CharField(verbose_name=_('current city'), max_length=40, default='', blank=True)
    street = models.CharField(verbose_name=_('street address'), max_length=200, default='', blank=True)
    about_self = models.TextField(verbose_name=_('About Yourself'), default='')
    logins = models.PositiveIntegerField(default=1)
    joined_date = models.DateField(auto_now_add=True)
    joined_time = models.TimeField(auto_now_add=True)

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        ),
    )
    # is_superuser field provided by PermissionsMixin
    # groups field provided by PermissionsMixin
    # user_permissions field provided by PermissionsMixin

    # date_joined = models.DateTimeField(
    #     _('date joined'), default=timezone.now
    # )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return '{} <{}>'.format(self.get_full_name(), self.email)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class MailSent(models.Model):
	sent_to = models.ForeignKey(User, on_delete=models.CASCADE)
	sent_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
	status = models.CharField(_('Message Status'), max_length=100, default='pending')
	date_sent = models.DateField(_('Date Sent'), auto_now_add=True)
	time_sent = models.TimeField(_('Time Sent'), auto_now_add=True)

	def __str__(self):
		return self.sent_to.first_name + ' ' + self.sent_to.last_name


class LoginCount(models.Model):
    log_user = models.ForeignKey(User, on_delete=models.CASCADE)
    browser = models.CharField(max_length=100, default='', blank=True)
    ip_address = models.CharField(max_length=100, default='', blank=True)
    date_sent = models.DateField(_('Date Sent'), auto_now_add=True)
    time_sent = models.TimeField(_('Time Sent'), auto_now_add=True)

    def __str__(self):
        return self.log_user.first_name + ' ' + self.log_user.last_name
