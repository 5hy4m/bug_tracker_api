from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    Name = models.CharField(max_length=200)
    Image = models.URLField(blank=True,default = None)
    Created_By = models.OneToOneField( User, on_delete=models.CASCADE )
    Created_On = models.DateTimeField(auto_now_add = True)
    Modified_On = models.DateTimeField(auto_now = True)
    Private = models.BooleanField(null=False)

class Shared_Board(models.Model):
    Board = models.ForeignKey(Board, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Is_Active = models.BooleanField(null=False)
    Created_On = models.DateTimeField(auto_now_add = True)
    Modified_On = models.DateTimeField(auto_now = True)

class Recently_Viewed_Board(models.Model):
    Board = models.ForeignKey(Board, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Is_Active = models.BooleanField(null=False)
    Created_On = models.DateTimeField(auto_now_add = True)
    Modified_On = models.DateTimeField(auto_now = True)

class List(models.Model):
    Name = models.CharField(max_length=50)
    Board = models.OneToOneField( Board, on_delete=models.CASCADE )

class Card(models.Model):
    Color = models.CharField(max_length=20)
    Name = models.CharField(max_length=50)
    Description = models.TextField()
    List = models.OneToOneField( List, on_delete=models.CASCADE )

class User_Activity(models.Model):
    Name = models.CharField(max_length=50)
    Description = models.CharField(max_length=250)
 
class Recent_Activity(models.Model):
    User = models.ForeignKey(User, on_delete=models.PROTECT ,null=False)
    Activity = models.ForeignKey(User_Activity, on_delete=models.PROTECT ,null=False)
    Board = models.ForeignKey(Board, on_delete=models.PROTECT ,null=True)
    List = models.ForeignKey(List, on_delete=models.PROTECT ,null=True)
    Card = models.ForeignKey(Card, on_delete=models.PROTECT ,null=True)
    Created_On = models.DateTimeField(auto_now_add = True)

