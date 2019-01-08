from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    steamid = models.CharField(default='0', max_length=20)

    def __str__(self):
        return f'{self.user.username} Profile'
