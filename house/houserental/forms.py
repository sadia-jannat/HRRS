import django
from django.contrib.auth import models
from django.core import validators
from django import forms
from django.forms import fields, widgets
from django import forms

#django form create kore bellow models and forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

#project form create use model
from .models import  ownerformfill,houserate,map

#ownerformfill model ar forms create for edit and delete create
class ownerformfillform(forms.ModelForm):
    class Meta:
        model=ownerformfill
        fields=['ownername', 'email', 'phn', 'housecategory', 'housename', 'houserent', 
        'img', 'imgidfont', 'imgidback', 'division','district', 'area', 'housesize',
     'bedroom', 'dinning', 'drawing', 'bathroom', 'kitchen', 'balcony',
    'allinfo']
        

#houserate model ar form houserateform
class houserateform(forms.ModelForm):
    class Meta:
        model=houserate
        fields=['info_review', 'info_rate']


#again map form..work
class mapformagain(forms.ModelForm):

    address=forms.CharField(label='')

    class Meta:
        model=map
        fields=['address',]  


#query for search
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
    
    
#here django create his own model and forms..we use their form and model auto create
# class name dilm ami..{SignUp}
class Create(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2' ]
                              