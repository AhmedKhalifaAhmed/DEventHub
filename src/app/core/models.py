from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .user_managers import UserManager

# Create custom user
class User(AbstractBaseUser, PermissionsMixin):
  '''
  Custom user with email auth and no username
  '''
  # Fields
  email = models.EmailField(_('email address'), unique=True, blank=False, max_length=254)
  first_name = models.CharField(_('first name'), blank=False, max_length=256)
  last_name = models.CharField(_('last name'), blank=False, max_length=256)
  date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
  is_active = models.BooleanField(_('active'), default=True)
  is_admin = models.BooleanField(_('staff status'), default=False)
  is_staff = models.BooleanField(_('admin status'), default=False)
  is_superuser = models.BooleanField(_('superuser status'), default=False)

  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name']

  class Meta:
    verbose_name = _('user')
    verbose_name_plural = _('users')
  
  def get_full_name(self):
    '''
    Returns the full name for the user.
    '''
    full_name = '{} {}'.format(self.first_name, self.last_name)
    return full_name.strip()
  
  def get_short_name(self):
    '''
    Returns the short name for the user.
    '''
  
  def email_user(self, subject, message, from_email=None, **kwargs):
    '''
    Sends an email to this User.
    '''
    send_mail(subject, message, from_email, [self.email], **kwargs)
    