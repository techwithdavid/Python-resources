from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, phone, **extra_fields):
        if not email:
            raise ValueError("Email debe ser provisto")
        if not password:
            raise ValueError("Contrasena debe ser provisto")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name, phone, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, first_name, last_name, phone, **extra_fields)

    def create_superuser(self, email, password, first_name, last_name, phone, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, first_name, last_name, phone, **extra_fields)

# class User(models.Model):
# class User(AbstractUser):
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        db_index=True, max_length=50, null=True, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(db_index=True, unique=True)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    direccion = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    # is_superuser = models.BooleanField(default=False)
    # is_verified = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    # lookup_field = 'username'
    objects = CustomUserManager()

    def __str__(self):
        # return self.is_email_verified
        return str(self.username, self.first_name, self.last_name, self.email, self.password)
