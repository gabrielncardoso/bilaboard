from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)

class Group(models.Model):
    name = models.CharField(max_length=30)
    players = models.ManyToManyField(User)

class Game(models.Model):
    name = models.CharField(max_length=50)
    #TRY TO USE AN EXISTING DATABASE

class Match(models.Model):
    datetime = models.DateTimeField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class Result(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.IntegerField()