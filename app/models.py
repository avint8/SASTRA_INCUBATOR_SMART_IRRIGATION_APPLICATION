from django.db import models
from django.contrib.auth.models import User

class apidata(models.Model):
    moisterlvl = models.IntegerField()
    motorruntime = models.IntegerField()
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)