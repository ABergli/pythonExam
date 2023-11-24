

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/images/', null=True, blank=True)
    video = models.FileField(upload_to='blog/videos/', null=True, blank=True)

    def __str__(self):
        return self.title



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    objects = CustomUserManager()

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name ='groups',
        blank = True,
        help_text ='The groups this user belongs to.',
        related_name ='customuser_set',  # Add this line
        related_query_name ='user',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name ='user permissions',
        blank = True,
        help_text ='Specific permissions for this user.',
        related_name ='customuser_set',  # Add this line
        related_query_name ='user',
    )

    def __str__(self):
        return self.username
