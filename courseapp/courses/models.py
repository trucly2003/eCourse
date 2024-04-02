from django.db import models
from  django.contrib.auth.models import AbstractUser

# Viết các lớp ở đây

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
    image = models.ImageField(upload_to='courses/%Y/%m')
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    tag = models.ManyToManyField('Tags')

    def __str__(self):
        return self.subject

    class Meta:
        unique_together = ('subject', 'category')
class Lesson(BaseModel):
    subject = models.CharField(max_length=250, null=False)
    description = models.TextField()
    image = models.ImageField(upload_to='lessons/%Y/%m')
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    tag = models.ManyToManyField('Tags')

    class Meta:
        unique_together = ('subject', 'course')

class Tags(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name