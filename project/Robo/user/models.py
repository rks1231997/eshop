from django.db import models
import datetime



class RoboData(models.Model):
    roboId = models.AutoField(primary_key = True)
    Status = models.CharField(max_length=100)
    roboDate = datetime.datetime.now()
