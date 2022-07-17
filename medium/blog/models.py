
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')