from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.


class UserManager(BaseUserManager):
    """
     user manager class  manage abstract base user
    """
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError('email is required')
        if not username:
            raise ValueError('username can not empty it is required')
        if not first_name:
            raise ValueError('mandatory field')
        if not last_name:
            raise ValueError('mandatory field')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name, last_name, username, email, password=None):
        """
        create superuser here
        Creates and saves a superuser with the given email and password.
        :param first_name:  save superuser with the given fist_name when create superuser
        :param last_name: save superuser with the given last_name when create superuser
        :param username: save superuser with the given username when create superuser
        :param email: save superuser with the given email when create superuser
        :param password: save superuser with the given password when create superuser
        :return: user to create user
        """
        if password is None:
            raise TypeError('Password should not be none')
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )
        user.is_superuser=True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    User is custom user to create table in database
    """
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    objects = UserManager()

    def __str__(self):
        return self.email

    def token(self):
        return ''

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_lebel):
        return True