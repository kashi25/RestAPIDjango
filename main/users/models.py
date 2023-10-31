from django.db import models
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible
import os


# Create your models here.

# for storing image filed another class is created

@deconstructible
class GenerateProfileImgaepath(object):
    def __init__(self):
        pass
    
    def __call__(self, instance, filename):
        ext = filename.splite('.')[-1]
        path = f'media/acounts/{instance.user.id}/images/'
        name = f'profile_image.{ext}'
        return os.path(path, name)
user_profile_image_path = GenerateProfileImgaepath()
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to= user_profile_image_path, blank=True,null=True)
    
    
    def __str__(self):
        return f'{self.user.username}\s Profile'