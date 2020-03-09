from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pet(models.Model):
    # user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='pets', blank=True, null=True)
    likes =  models.IntegerField(default = 0) 
    created = models.DateTimeField(auto_now_add=True, editable=False)
    def __str__(self):
        return self.title