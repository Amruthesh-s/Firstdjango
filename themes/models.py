from django.db import models

# Create your models here.
class SitesSetting(models.Model):
    banner=models.ImageField(upload_to='image')
    caption=models.TextField()
    

