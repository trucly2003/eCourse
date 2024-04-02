from django.db import models
from  django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class BaseModel(models.Model):
    create_date = models.DateField(auto_now=True)
    updated_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Courses(BaseModel):
    subject = models.CharField(max_length=250, null=False)
    description = models.TextField()

    image = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject