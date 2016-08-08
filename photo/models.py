from django.contrib.auth.models import User
from django.db import models
from sorl.thumbnail import ImageField


class Photo(models.Model):
    user = models.ForeignKey(User)
    image = ImageField(upload_to='photo')
