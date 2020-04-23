from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class BaseUser(AbstractUser):
    # username = None
    email = models.EmailField(max_length=255, unique=True)


    # USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['email']

    # def get_username(self):
    #     return self.email


class Student(BaseUser):
    dept = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    roll = models.PositiveIntegerField()
    cgpa = models.DecimalField(decimal_places=2,max_digits=4)


    class Meta:
        verbose_name = 'Students'
        verbose_name_plural = 'Students'

class Professor(BaseUser):
    dept = models.CharField(max_length=100)
    research_area = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Professors'
        verbose_name_plural = 'Professors'
