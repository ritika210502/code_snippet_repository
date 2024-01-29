from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Code(models.Model):
    title=models.CharField(max_length=250)
    code_content=models.TextField()
    language=models.CharField(max_length=50)
    tags=models.CharField(max_length=250,blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
