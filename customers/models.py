from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class Customer(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live')),((DELETE,'Delete'))
    name=models.TextField()
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user')
    phone=models.CharField(max_length=10)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


def __str__(self) -> str:
    return self.title

