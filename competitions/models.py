from django.db import models
from django.contrib.auth.models import User
from django_quill.fields import QuillField
from django.urls import reverse
from django.utils.text import slugify
from django.core.exceptions import ValidationError
import datetime
# Create your models here.

def CheckDateStart(passed_date):
    if passed_date < datetime.date.today():
        raise ValidationError(u'The given date is not a valid one! Please choose a coming date!')
    #if (passed_date + datetime.date.today()).days > 400:
        #raise ValidationError(u'The given date is not a valid one! Please choose a closer date or add this competiton later!')

class Competition(models.Model):
    Competition_Title = models.CharField(max_length=200, unique=True)
    Registration_Start_Date = models.DateField(auto_now=False, auto_now_add=False,validators=[CheckDateStart])
    Registration_End_Date = models.DateField(auto_now=False, auto_now_add=False, validators=[CheckDateStart])
    Competition_Details = QuillField()
    Registered_Users = models.ManyToManyField(User, blank=True)
    Competition_Graphic = models.ImageField(null=True, blank=True, upload_to='competitions/graphics/')
    Competition_Category = models.CharField(max_length=255, default="Web Development")
    slug = models.SlugField(default="competiton", unique=True)
    def __str__(self):
        return f"{self.Competition_Title}"
    def save(self, *args, **kwargs):
        value = self.Competition_Title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class Categories(models.Model):
    Category_Name = models.CharField(max_length=200)
    Category_Code = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return f"{self.Category_Name} | {self.Category_Code}"
