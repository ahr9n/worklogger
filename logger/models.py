from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class Log(models.Model):
    duration = models.FloatField(default=0)
    day = models.DateField(default=datetime.date.today)
    description = models.CharField(max_length=256)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    project = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.duration}, {self.user} - {self.project.title}"
