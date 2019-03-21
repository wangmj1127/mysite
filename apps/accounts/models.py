from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


# Create your models here.

class UserAccount(AbstractUser):
    nickname = models.CharField('Name', max_length=100, blank=True)
    mugshot = models.ImageField('Photo', upload_to='upload/mugshots', blank=True,
                                default='upload/mugshots/logo.jpg')
    created_time = models.DateTimeField('Create Time', default=now)
    last_mod_time = models.DateTimeField('Modify Time', default=now)

    # objects = BlogUserManager()
    def __str__(self):
        return self.email
