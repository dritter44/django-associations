from django.db import models

# Create your models here.
'''actors fields
-first name
-last name
-born: date, cannot be null
-died: date, can be null
-spouse: can be null


movie fields:
-title
-release year
-rating
-length
-director
-writer


roles:
-movie: foreign key
-actor: foreign key
-first name
-last name
-description
'''
class Actor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField(auto_now=False,auto_now_add=False, null=True)

class Movie(models.Model):
    title = models.CharField(max_length=255, null=False)
    release_date= models.DateField(auto_now=False,auto_now_add=False, null=True)
    length = models.TimeField(auto_now=False,auto_now_add=False, null=True)
    director = models.CharField(max_length=255, null=True)
    writer = models.CharField(max_length=255, null=True)
    actors = models.ManyToManyField(Actor, related_name='movies',through='Role')

class Role(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name= 'roles')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name= 'roles')
