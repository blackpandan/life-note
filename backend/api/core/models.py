from django.db import models

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=225)
    body=models.CharField(max_length=225)
    done=models.BooleanField(default=False)
    pause=models.BooleanField(default=False)

class Project(models.Model):
    title=models.CharField(max_length=255)
    body=models.TextField()
    time = models.DateTimeField(auto_now_add=True)
