from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Competition, Categories
from django_quill.forms import QuillFormField
from datetime import datetime

categories = Categories.objects.all().values_list('Category_Name', 'Category_Name')
choices = []

for category in categories:
    choices.append(category)

class CreateCompetitionForm(forms.ModelForm):
        Competition_Title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Create a name for your competition'}))
        Registration_Start_Date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'col-sm-3 me-2 mb-3'}))
        Registration_End_Date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'col-sm-3 me-2 mb-3'}))
        Competition_Details = QuillFormField()
        Competition_Graphic = forms.ImageField(allow_empty_file=True, widget=forms.FileInput(attrs={'class': 'form-control mb-3'}))
        Competition_Category = forms.ChoiceField(choices = choices, widget=forms.Select(attrs={'class': 'form-control mb-3'}))
        class Meta:
            model = Competition
            fields = ('Competition_Title', 'Registration_Start_Date', 'Registration_End_Date', 'Competition_Details', 'Competition_Graphic', 'Competition_Category')

class EditCompetitionForm(forms.ModelForm):
        Competition_Title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Create a name for your competition'}))
        Registration_Start_Date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'col-sm-3 me-2 mb-3'}))
        Registration_End_Date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'col-sm-3 me-2 mb-3'}))
        Competition_Details = QuillFormField()
        Competition_Graphic = forms.ImageField(allow_empty_file=True, widget=forms.FileInput(attrs={'class': 'form-control mb-3'}))
        Competition_Category = forms.ChoiceField(choices = choices, widget=forms.Select(attrs={'class': 'form-control mb-3'}))
        class Meta:
            model = Competition
            fields = ('Competition_Title', 'Registration_Start_Date', 'Registration_End_Date', 'Competition_Details', 'Competition_Graphic', 'Competition_Category')
