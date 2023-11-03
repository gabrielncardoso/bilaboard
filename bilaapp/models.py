from django.db import models
from django.contrib.auth.models import User

#class User(models.User):
    #name = models.CharField(max_length=30)

    #def __str__(self):
        #return self.name

class Group(models.Model):
    name = models.CharField(max_length=30)
    players = models.ManyToManyField(User)

class Game(models.Model):
    name = models.CharField(max_length=50)
    #TRY TO USE AN EXISTING DATABASE

class Match(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class Result(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.IntegerField()