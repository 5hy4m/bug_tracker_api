from django.db import models

class User(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=254)
    Created_On = models.DateTimeField(auto_now_add = true)
    Modified_On = models.DateTimeField(auto_now = true)

class Board(models.Model):
    Name = models.CharField(max_length=200)
    Image = models.UrlField()
    Created_By = models.OneToOneField( User, on_delete=models.CASCADE )
    Created_On = models.DateTimeField(auto_now_add = true)
    Modified_On = models.DateTimeField(auto_now = true)
    Private = models.BooleanField(null=False)

class Shared_Board(models.Model):
    Board = models.ForeignKey(Board, on_delete=models.CASCADE)
    User = models.ForeignKey(Board, on_delete=models.CASCADE)
    Is_Active = models.ForeignKey(Board, on_delete=models.CASCADE)
    Created_On = models.DateTimeField(auto_now_add = true)
    Modified_On = models.DateTimeField(auto_now = true)

class Recently_Viewed_Board(models.Model):
    Board = models.ForeignKey(Board, on_delete=models.CASCADE)
    User = models.ForeignKey(Board, on_delete=models.CASCADE)
    Is_Active = models.ForeignKey(Board, on_delete=models.CASCADE)
    Created_On = models.DateTimeField(auto_now_add = true)
    Modified_On = models.DateTimeField(auto_now = true)

class List(models.Model):
    Name = models.CharField(max_length=50)
    Board = models.OneToOneField( Board, on_delete=models.CASCADE )

class Card(models.Modal):
    Color = models.CharField(max_length=20)
    Name = models.CharField(max_length=50)
    Description = models.TextField()
    List = models.OneToOneField( List, on_delete=models.CASCADE )

class User_Activity():
    Name = models.CharField(max_length=50)
    Description = models.CharField(max_length=250)
 
class Recent_Activity(models.Model):
    User = models.ForeignKey(Board, on_delete=models.PROTECT ,null=False)
    Activity = models.ForeignKey(User_Activity, on_delete=models.PROTECT ,null=False)
    Board = models.ForeignKey(Board, on_delete=models.PROTECT ,null=True)
    List = models.ForeignKey(List, on_delete=models.PROTECT ,null=True)
    Card = models.ForeignKey(Card, on_delete=models.PROTECT ,null=True)
    Created_On = models.DateTimeField(auto_now_add = true)

