from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser) :
    pass

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=True )
    update_date = models.DateTimeField(auto_now=True, null=True )
    active = models.BooleanField(default=True, null=True )

    class Meta:
        abstract = True
# Create your models here.
class Category ( BaseModel):
    name = models.CharField(max_length=50, null= False)

    def __str__(self):
        return self.name

class Course (models.Model ):
    subject = models.CharField(max_length=255,null =False)
    description = models.TextField()
    image = models.CharField(max_length=100 )

    category = models.ForeignKey(Category, on_delete =models.CASCADE)
    def __str__(self):
        return self.subject