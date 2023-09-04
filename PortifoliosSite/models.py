from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    photo = models.ImageField(upload_to='user')
    github = models.URLField( null= True)
    linkedin = models.URLField(null=True)

    def __str__(self) -> str:
        return self.username

class Project(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    resumo = models.TextField(max_length=499)
    content = models.TextField()
    image_1 = models.ImageField(upload_to='project')
    image_2 = models.ImageField(upload_to='project')
    image_3 = models.ImageField(upload_to='project')
    github = models.URLField( null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
