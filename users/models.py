from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    image= models.ImageField(default='profilepic.jpg',upload_to='profile_pictures')
    location= models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.user.username
# Create your models here.
