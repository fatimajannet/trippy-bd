from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import uuid


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    u_id        = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username    = models.CharField(max_length=150, unique=True)
    email       = models.EmailField(unique=True)

    
    fname       = models.CharField(max_length=50)
    mname       = models.CharField(max_length=50, blank=True, null=True)
    lname       = models.CharField(max_length=50)

    u_location  = models.CharField(max_length=255, blank=True, null=True)

    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='accounts_user_set',
        related_query_name='accounts_user',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='accounts_user_set',
        related_query_name='accounts_user',
        verbose_name='user permissions',
    )

    objects = UserManager()

    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['email', 'fname', 'lname']

    def get_full_name(self):
        if self.mname:
            return f"{self.fname} {self.mname} {self.lname}"
        return f"{self.fname} {self.lname}"

    def __str__(self):
        return self.username