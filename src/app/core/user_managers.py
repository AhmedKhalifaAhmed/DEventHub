from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
  use_in_migrations = True

  def _create_user(self, user, email, password, **extra_fields):
    '''
    creates and saves a user with the given email and password (Not used directly).
    '''
  
  def create_user(self, email, password=None, **extra_fields):
    '''
    Create a normal user
    '''
    extra_fields.setdefault('is_supseruser', False)
    if not email:
      raise ValueError('Email field is required')
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user
  
  def create_superuser(self, email, password, **extra_fields):
    '''
    Create a super user
    '''
    extra_fields.setdefault('is_superuser', True)
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_admin', True)
    if extra_fields.get('is_superuser') is not True:
      raise ValueError('Superuser must have is_superuser=True.')
    if not email:
      raise ValueError('Email field is required')
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user
